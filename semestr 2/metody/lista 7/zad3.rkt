#lang racket

(struct variable     (id)        #:transparent)
(struct quantifier   (q id expr) #:transparent)
(struct l-binop      (op l r)    #:transparent)
(struct l-unop       (op e)      #:transparent)
(struct const        (val)       #:transparent)

(define (quantif? q)
    (member q '(A E)))

(define (b-operator? x)
    (member x '(& v =>)))

(define (u-operator? x)
  (member x '(~)))

(define (bool? x)
  (member x '(#t #f)))

(define (expr? e)
  (match e
    [(const x) (bool? x)]
    [(variable x) (symbol? x)]
    [(l-binop op l r) (and (b-operator? op) (expr? l) (expr? r))]
    [(l-unop op e) (and (u-operator? op) (expr? e))]
    [(quantifier q id expr) (and (quantifier? q) (variable? id) (expr? expr))]))

(define (parse e)
  (cond
    [(bool? e) (const e)]
    [(and (list? e) (= (length e) 3) (quantif? (car e))) (quantifier (car e) (cadr e) (parse (caddr e)))]
    [(and (list? e) (= (length e) 3) (b-operator? (car e))) (l-binop (car e) (parse (cadr e)) (parse (caddr e)))]
    [(and (list? e) (= (length e) 2) (u-operator? (car e))) (l-unop (car e) (parse (cadr e)))]
    [(symbol? e) (variable e)]))

(parse '(A x (& #t x)))