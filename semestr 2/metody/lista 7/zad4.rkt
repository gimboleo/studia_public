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
  (member x (list #t #f)))

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

(define (subst id e expr)
  (match expr
    [(variable x) (if (eq? id x) e expr)]
    [(const v) expr]
    [(l-binop op l r) (l-binop op (subst id e l) (subst id e r))]
    [(l-unop op l) (l-unop op (subst id e l))]
    [(quantifier q x ex) (eq? id x) expr (quantifier q x (subst id e ex))]))

(define (op->proc op)
  (match op
    ['& (lambda (a b) (and a b))]
    ['v (lambda (a b) (or a b))]
    ['=> (lambda (a b) (or (not a) b))]
    ['~ (lambda (a) (not a))]))

(define (eval expr)
  (match expr
    [(const v) v]
    [(variable x) (error "No bueno")]
    [(l-binop op l r) ((op->proc op) (eval l) (eval r))]
    [(l-unop op e) ((op->proc op) (eval e))]
    [(quantifier 'A id e) (and (eval (subst id (const #f) e)) (eval (subst id (const #t) e)))]
    [(quantifier 'E id e) (or (eval (subst id (const #f) e)) (eval (subst id (const #t) e)))]))

(eval (parse '(E x (~ x))))
(eval (parse '(& #t #f)))
(eval (parse #f))
(eval (parse '(A x (=> #f x))))
(eval (parse '(E x (A y (=> x y)))))
(eval (parse '(A x (A y (=> x y)))))
(eval (parse '(A x (E x (=> x x)))))