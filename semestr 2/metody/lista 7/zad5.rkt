#lang racket

(struct const (val) #:transparent)
(struct binop (op l r) #:transparent)
(struct var-expr (id) #:transparent)
(struct let-expr (id e1 e2) #:transparent)
(struct environ (xs))

(define (operator? x)
  (member x '(+ - * /)))

(define (expr? e)
  (match e
    [(const n) (number? n)]
    [(binop op l r) (and (operator? op) (expr? l) (expr? r))]
    [(var-expr x) (symbol? x)]
    [(let-expr x e1 e2) (and (symbol? x) (expr? e1) (expr? e2))]
    [_ false]))

(define (parse e)
  (cond
    [(number? e) (const e)]
    [(symbol? e) (var-expr e)]
    [(and (list? e) (eq? (length e) 3) (eq? (first e) 'let))
     (let-expr (first (second e))
               (parse (second (second e)))
               (parse (third e)))]
    [(and (list? e) (eq? (length e) 3) (operator? (first e)))
     (binop (first e) (parse (second e)) (parse (third e)))]))



(define env-empty (environ null))

(define (env-lookup x env)
  (define (aux xs)
    (cond
      [(null? xs) #f]
      [(eq? x (caar xs)) (car xs)]
      [else (aux (cdr xs))]))
  (aux (environ-xs env)))

(define (env-add x env)
  (define (aux xs)
    (cond
      [(null? xs) (list (cons x 1))]
      [(eq? x (caar xs)) (cons (cons x (+ (cdar xs) 1)) (cdr xs))]
      [else (cons (car xs) (aux (cdr xs)))]))
  (environ (aux (environ-xs env))))

(define (name x number)
  (string->symbol (string-append (symbol->string x) (number->string number))))

(define (rename-env expr env)
  (match expr
    [(const n) expr]
    [(binop op l r) (binop op (rename-env l env) (rename-env r env))]
    [(let-expr x e1 e2)
     (let* ((new-env (env-add x env))
            (aux (env-lookup x new-env))
            (new-x (name (car aux) (cdr aux))))
       (let-expr new-x (rename-env e1 env) (rename-env e2 new-env)))]
    [(var-expr x)
     (let ((aux (env-lookup x env)))
       (if (pair? aux)
           (var-expr (name (car aux) (cdr aux)))
           expr))]))

(define (rename expr) (rename-env expr env-empty))



(rename (binop '+ (let-expr 'x (const 1) (var-expr 'x)) (let-expr 'x (const 1) (var-expr 'x))))
(rename (let-expr 'x (binop '* (const 3) (var-expr 'x)) (binop '+ (var-expr 'x) (let-expr 'x (binop '* (var-expr 'x) (const 5)) (var-expr 'x)))))
(rename (let-expr 'x (const 3) (binop '+ (var-expr 'x) (let-expr 'x (const 5) (var-expr 'x)))))