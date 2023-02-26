#lang racket

(struct const (val) #:transparent)
(struct binop (op left right) #:transparent)

(define (operator? op)
  (member op '(+ - * /)))

(define (expr? e)
  (or (and (const? e)
           (number? (const-val e)))
      (and (binop? e)
           (operator? (binop-op e))
           (expr? (binop-left e))
           (expr? (binop-right e)))))

(define (value? e) (number? e))

(define (op->proc op)
  (match op
    ('+ +)
    ('- -)
    ('* *)
    ('/ (lambda (x y) (if (= y 0) (error "Division by zero") (/ x y))))))

(define (eval e)
  (match e
    [(const n) n]
    [(binop op el er)
     (let ((vl (eval el))
           (vr (eval er)))
       ((op->proc op) vl vr))]))

(define (pi-expr n)
  (define (num-pi i)
    (define (square x) (* x x))
    (square (- (* 2 i) 1)))
  (define (den-pi i) 6.0)
  (define (aux i)
    (if (< n i)
        (const 0)
        (binop '/ (const (num-pi i)) (binop '+ (const (den-pi i)) (aux (+ i 1))))))  
  (binop '+ (const 3) (aux 1)))


(pi-expr 2)
(eval (pi-expr 16))