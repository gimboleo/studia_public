#lang racket

(define (^ x y) (expt x y))
(define ($ x) (abs x))

(struct const (val) #:transparent)
(struct binop (op left right) #:transparent)
(struct unop (op val) #:transparent)

(define (operator? op)
  (member op '(+ - * / ^ $)))

(define (expr? e)
  (or (and (const? e)
           (number? (const-val e)))
      (and (binop? e)
           (operator? (binop-op e))
           (expr? (binop-left e))
           (expr? (binop-right e)))
      (and (unop? e)
           (operator? (unop-op e))
           (expr? (unop-val e)))))

(define (value? e) (number? e))

(define (op->proc op)
  (match op
    ('+ +)
    ('- -)
    ('* *)
    ('/ (lambda (x y) (if (= y 0) (error "Division by zero") (/ x y))))
    ('^ (lambda (x y) (if (< y 0) (error "Exponentation by negative number") (^ x y))))
    ('$ $)))

(define (eval e)
  (match e
    [(const n) n]
    [(binop op el er)
     (let ((vl (eval el))
           (vr (eval er)))
       ((op->proc op) vl vr))]
    [(unop op val) ((op->proc op) (eval val))]))

(define (parse e)
  (cond
    [(number? e) (const e)]
    [(and (list? e)
          (= 3 (length e))
          (operator? (car e)))
     (binop (car e) (parse (cadr e)) (parse (caddr e)))]
    [(and (list? e)
          (= 2 (length e))
          (operator? (car e)))
     (unop (car e) (parse (cadr e)))]
    [else (error "Parse error:" e)]))

(define 5+3^3
  (binop '+
         (const 5)
         (binop '^
                (const 3)
                (const 3))))

(define |4-3*2|
  (unop '$
        (binop '-
               (const 4)
               (binop '*
                      (const 3)
                      (const 2)))))

(parse '(+ 5 (^ 3 3)))
5+3^3
(eval 5+3^3)

(display "\n")

(parse '($ (- 4 (* 3 2))))
|4-3*2|
(eval |4-3*2|)