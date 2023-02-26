#lang racket

(struct const (val)           #:transparent)
(struct binop (op left right) #:transparent)
(struct unop (op arg)         #:transparent)
(struct der (arg)         #:transparent)
(struct variable ()    #:transparent)

(define (expr? e)
  (or (and (const? e)
           (number? (const-val e)))
      (variable? e)
      (and (binop? e)
           (operator? (binop-op e))
           (expr?     (binop-left e))
           (expr?     (binop-right e)))
      (and (unop? e)
           (operator? (unop-op e)
           (expr? (unop-arg e))))
      (and (der? e)
           (expr? (der-arg e)))))
     
(define (operator? op)
  (member op '(+ - * / ^ abs)))

(define (op->proc op)
  (match op
    ('+ +)
    ('- -)
    ('* *)
    ('/ (lambda (x y) (if (= y 0) (error "Division by zero") (/ x y))))
    ('^ expt)
    ('abs abs)))
    
(define (eval e x) ;; <- to jest interpreter/ewaluator!
  (match e
    [(const n) n]
    [(variable) x]
    [(binop op el er)
     (let ((vl (eval el x))
           (vr (eval er x)))
       ((op->proc op) vl vr))]
    [(unop op arg)
     ((op->proc op) (eval arg x))]
    [(der arg)
     (eval (∂ arg) x)]))
     
(define (parse e)
  (cond
    [(number? e) (const e)]
    [(eq? e 'x) (variable)]
    [(and (list? e)
          (= 3 (length e))
          (operator? (car e)))
     (binop (car e) (parse (cadr e)) (parse (caddr e)))]
    [(and (list? e)
          (= 2 (length e))
          (operator? (car e)))
     (unop (car e) (parse (cadr e)))]
    [(and (list? e)
          (= 2 (length e))
          (eq? '∂ (car e)))
     (der (parse (cadr e)))]
    [else (error "Parse error:" e)]))

(define (∂ e)
  (match e
    [(const n) (const 0)]
    [(variable) (const 1)]
    [(binop '+ l r) (binop '+ (∂ l) (∂ r))]
    [(binop '* l r) (binop '+ (binop '* (∂ l) r) (binop '* l (∂ r)))]
    [(der arg) (∂ (∂ arg))]))