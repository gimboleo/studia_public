#lang racket

(struct const    (val)                  #:transparent)
(struct unop     (op e)                 #:transparent)
(struct binop    (op l r)               #:transparent)
(struct var-expr (id)                   #:transparent)
(struct let-expr (id e1 e2)             #:transparent)
(struct acc-expr (op start end f x)     #:transparent)
(struct min-expr (f)                    #:transparent)

(define (operator? x)
  (member x '(+ - * / ^)))

(define (acc-operator? x)
  (member x '(integral bound-sum)))

(define (expr? e)
  (match e
    [(const n) (number? n)]
    [(unop  op e) (and (operator? op) (expr? e))]
    [(binop op l r) (and (operator? op) (expr? l) (expr? r))]
    [(var-expr x) (symbol? x)]
    [(let-expr x e1 e2) (and (symbol? x) (expr? e1) (expr? e2))]
    [(acc-expr op s e f x) (and (acc-operator? op) (expr? s) (expr? e) (expr? f) (expr? x))]
    [(min-expr f) (expr? f)]
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
            (parse (third q)))]
    [(and (list? q) (eq? (length q) 4) (acc-operator? (first q)))
      (acc-expr (first q)
                (parse (car (second q)))
                (parse (cadr (second q)))
                (parse (third q))
                (fourth q))]
    [(and (list? q) (eq? (length q) 2) (eq? 'min (first q)))
     (min-expr (parse (second q)))]))

(define (test2) (parse '(integral ((+ 1 1) +inf.0) (/ 1 (^ 2 x)) x)))
(test2)