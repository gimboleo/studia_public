#lang racket

(require racket/set)

; --------- ;
; Wyrazenia ;
; --------- ;

(struct const    (val)      #:transparent)
(struct binop    (op l r)   #:transparent)
(struct var-expr (id)       #:transparent)
(struct let-expr (id e1 e2) #:transparent)

(define (operator? x)
  (member x '(+ - * /)))

(define (expr? e)
  (match e
    [(const n) (number? n)]
    [(binop op l r) (and (operator? op) (expr? l) (expr? r))]
    [(var-expr x) (symbol? x)]
    [(let-expr x e1 e2) (and (symbol? x) (expr? e1) (expr? e2))]
    [_ false]))

(define (parse q)
  (cond
    [(number? q) (const q)]
    [(symbol? q) (var-expr q)]
    [(and (list? q) (eq? (length q) 3) (eq? (first q) 'let))
     (let-expr (first (second q))
               (parse (second (second q)))
               (parse (third q)))]
    [(and (list? q) (eq? (length q) 3) (operator? (first q)))
     (binop (first q)
            (parse (second q))
            (parse (third q)))]))

(define (test-parse) (parse '(let [x (+ 2 2)] (+ x 1))))

; -------------
; Wolne zmienne
; -------------

(define env-empty          (set))
(define (env-add x env)    (set-add env x))
(define (env-lookup x env) (set-member? env x))

(define (free-vars-env e env)
  (match e
    [(const n) (set)]
    [(binop op l r)
     (set-union (free-vars-env l env)
                (free-vars-env r env))]
    [(let-expr x e1 e2)
     (set-union (free-vars-env e1 env)
                (free-vars-env e2 (env-add x env)))]
    [(var-expr x)
     (if (env-lookup x env)
         (set) (list->set (list x)))]))

(define (free-vars e)
  (set->list (free-vars-env e env-empty)))

(define (test-free-vars)
  (free-vars (parse
    '(let [x (+ 2 y)]
       (let [z (+ z x)] ; tu zmienna z jest wolna!
         z)))))



(define (optimize e)
  (match e
    [(const n) e]
    [(binop op l r) (binop op (optimize l) (optimize r))]
    [(var-expr x) e]
    [(let-expr x e1 e2)
     (if (member x (free-vars e2))
         (let-expr x (optimize e1) (optimize e2))
         (optimize e2))]))

(optimize (let-expr 'x (binop '+ (const 2) (const 2))
                    (let-expr 'y (binop '* (const 3) (var-expr 'x))
                              (binop '+ (const 7) (var-expr 'x)))))