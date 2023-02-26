#lang racket

(struct const (val) #:transparent)
(struct binop (op left right) #:transparent)
(struct variable () #:transparent)

(define (operator? op)
  (member op '(+ - * /)))

(define (expr? e)
  (or (and (const? e)
           (number? (const-val e)))
      (and (binop? e)
           (operator? (binop-op e))
           (expr? (binop-left e))
           (expr? (binop-right e)))
      (variable?)))

(define (value? e) (number? e))

(define (op->proc op)
  (match op
    ('+ +)
    ('- -)
    ('* *)
    ('/ (lambda (x y) (if (= y 0) (error "Division by zero") (/ x y))))))

(define (eval e val)
  (match e
    [(const n) n]
    [(variable) val]
    [(binop op el er)
     (let ((vl (eval el val))
           (vr (eval er val)))
       ((op->proc op) vl vr))]))

(define (parse e)
  (cond
    [(number? e) (const e)]
    [(and (list? e)
          (= 3 (length e))
          (operator? (car e)))
     (binop (car e) (parse (cadr e)) (parse (caddr e)))]
    [(eq? e 'x) (variable)]
    [else (error "Parse error:" e)]))

(define (∂ e)
  (match e
    [(const n) (const 0)]
    [(variable) (const 1)]
    [(binop '+ l r) (binop '+ (∂ l) (∂ r))]
    [(binop '* l r) (binop '+ (binop '* (∂ l) r) (binop '* l (∂ r)))]))
    


(define x^3
  (binop '* (variable)
         (binop '* (variable)
                (variable))))

x^3
(eval (∂ x^3) 1)
(eval (∂ x^3) 2)
(eval (∂ x^3) 3)