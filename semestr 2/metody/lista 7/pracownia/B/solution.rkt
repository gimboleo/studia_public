#lang racket

(require rackunit)
(provide (struct-out const) (struct-out binop) (struct-out var-expr) (struct-out let-expr) (struct-out var-dead) find-dead-vars)

; --------- ;
; Wyrazenia ;
; --------- ;

(struct const    (val)      #:transparent)
(struct binop    (op l r)   #:transparent)
(struct var-expr (id)       #:transparent)
(struct var-dead (id)       #:transparent)
(struct let-expr (id e1 e2) #:transparent)

(define (expr? e)
  (match e
    [(const n) (number? n)]
    [(binop op l r) (and (symbol? op) (expr? l) (expr? r))]
    [(var-expr x) (symbol? x)]
    [(var-dead x) (symbol? x)]
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
    [(and (list? q) (eq? (length q) 3) (symbol? (first q)))
     (binop (first q)
            (parse (second q))
            (parse (third q)))]))

; ---------------------------------- ;
; Wyszukaj ostatnie uzycie zmiennych ;
; ---------------------------------- ;

(define (find-x x e)
  (match e
    [(const n) #f]
    [(binop op l r) (or (find-x x l) (find-x x r))]
    [(var-expr v) (if (eq? v x) #t #f)]
    [(var-dead v) #f]
    [(let-expr v e1 e2) (if (eq? v x) (find-x x e1) (or (find-x x e1) (find-x x e2)))]))

(define (find-dead-vars e)
  (match e
    [(const n) e]
    [(binop op l r) (binop op (find-dead-vars l) (find-dead-vars r))]
    [(var-expr x) e]
    [(var-dead x) e]
    [(let-expr x e1 e2) (let-expr x (find-dead-vars e1) (aux x e2))]))

(define (aux x e)
  (match e
    [(const n) e]
    [(binop op l r) (if (find-x x r) (binop op (find-dead-vars l) (aux x r)) (binop op (aux x l) (find-dead-vars r)))]
    [(var-expr v) (if (eq? v x) (var-dead x) e)]
    [(var-dead v) e]
    [(let-expr v e1 e2) (if (eq? v x)
                            (let-expr v (aux x e1) (aux v e2))
                            (if (find-x x e2)
                                (let-expr v e1 (aux v (aux x e2)))
                                (let-expr v (aux x e1) (aux v e2))))]))



(check-equal? (find-dead-vars (let-expr 'x (const 3) (binop '+ (var-expr 'x) (var-expr 'x))))
              (let-expr 'x (const 3) (binop '+ (var-expr 'x) (var-dead 'x))))

(check-equal? (find-dead-vars (let-expr 'x (const 3) (binop '+ (var-expr 'x) (let-expr 'x (const 5) (binop '+ (var-expr 'x) (var-expr 'x))))))
              (let-expr 'x (const 3) (binop '+ (var-dead 'x) (let-expr 'x (const 5) (binop '+ (var-expr 'x) (var-dead 'x))))))

(check-equal? (find-dead-vars (let-expr 'x (const 3) (binop '+ (var-expr 'x) (let-expr 'x (let-expr 'x (const 4) (var-expr 'x)) (binop '+ (var-expr 'x) (var-expr 'x))))))
              (let-expr 'x (const 3) (binop '+ (var-dead 'x) (let-expr 'x (let-expr 'x (const 4) (var-dead 'x)) (binop '+ (var-expr 'x) (var-dead 'x))))))

(check-equal? (find-dead-vars (binop '*
                                     (let-expr 'y (const 1)
                                               (let-expr 'x (const 2)
                                                         (binop '+ (let-expr 'y (var-expr 'x) (binop '+ (var-expr 'y) (var-expr 'x)))
                                                                (var-expr 'y))))
                                     (let-expr 'x (const 10)
                                               (let-expr 'y (const 12)
                                                         (binop '/ (var-expr 'y)
                                                                (binop '+ (var-expr 'y) (var-expr 'x)))))))
              (binop
               '*
               (let-expr 'y (const 1) (let-expr 'x (const 2) (binop '+ (let-expr 'y (var-expr 'x) (binop '+ (var-dead 'y) (var-dead 'x))) (var-dead 'y))))
               (let-expr 'x (const 10) (let-expr 'y (const 12) (binop '/ (var-expr 'y) (binop '+ (var-dead 'y) (var-dead 'x)))))))