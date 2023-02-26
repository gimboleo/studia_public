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

(define (priority op)
  (match op
    ('+ 2)
    ('- 2)
    ('* 1)
    ('/ 1)))

(define (pretty-print ex)
  (match ex
    [(const n) (number->string n)]
    [(binop op el er) (string-append "("
                                     (pretty-print el)
                                     (symbol->string op)
                                     (pretty-print er)
                                     ")")]))

(define (pretty-print-harder ex)
  (match ex
    [(const n) (number->string n)]
    [(binop op el er)
     (cond [(and (and (binop? el) (> (priority (binop-op el)) (priority op))) (and (binop? er) (> (priority (binop-op er)) (priority op))))
            (string-append "(" (pretty-print-harder el) ")" (symbol->string op) "(" (pretty-print-harder er) ")")]
           [(and (binop? el) (> (priority (binop-op el)) (priority op)))
            (string-append "(" (pretty-print-harder el) ")" (symbol->string op) (pretty-print-harder er))]
           [(and (binop? er) (> (priority (binop-op er)) (priority op)))
            (string-append (pretty-print-harder el) (symbol->string op) "(" (pretty-print-harder er) ")")]
           [else (string-append (pretty-print-harder el) (symbol->string op) (pretty-print-harder er))])]))



(define 5+3*3
  (binop '+
         (const 5)
         (binop '*
                (const 3)
                (const 3))))

(define 5*6
  (binop '*
         (const 5)
         (binop '+
                (const 3)
                (const 3))))

(pretty-print 5+3*3)
(pretty-print-harder 5+3*3)

(display "\n")

(pretty-print 5*6)
(pretty-print-harder 5*6)