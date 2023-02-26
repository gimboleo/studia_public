#lang racket

(require rackunit)
(provide (struct-out const) (struct-out binop) rpn->arith)

(define (rpn-expr? e)
  (and (list? e)
       (pair? e)
       (andmap (lambda (x) (or (number? x) (member x '(+ - * /)))) e)))

(struct const (val) #:transparent)
(struct binop (op l r) #:transparent)

(define (arith-expr? e)
  (match e
    [(const n) (number? n)]
    [(binop op l r) (and (symbol? op) (arith-expr? l) (arith-expr? r))]
    [_ false]))



(define (rpn->arith e)
  (define (aux e acc)
    (if (null? e)
        (car acc)
        (match (car e)
          [(? number?) (aux (cdr e) (cons (const (car e)) acc))]
          [(or '+ '- '* '/) (aux (cdr e) (cons
                                          (binop (car e) (cadr acc) (car acc))
                                          (cddr acc)))])))
  (aux e null))

(check-equal? (rpn->arith '(1 2 -)) (binop '- (const 1) (const 2)))
(check-equal? (rpn->arith '(2 7 + 3 / 14 3 - 4 * + 2 /)) (binop '/
                                                                (binop '+
                                                                       (binop '/
                                                                              (binop '+ (const 2) (const 7))
                                                                              (const 3))
                                                                       (binop '*
                                                                              (binop '- (const 14) (const 3))
                                                                              (const 4)))
                                                                (const 2)))