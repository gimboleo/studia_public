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
    
(define (simpl e)
  (match e
    [(variable) (variable)]
    [(const val) (const val)]
    [(binop op el er)
     (let* ((l (simpl el))
            (r (simpl er))
            (e (binop op l r)))
       (match e
         [(binop '+ (const 0) r) r]
         [(binop '+ l (const 0)) l]
         [(binop '+ v v) (binop '* (const 2) v)]
         [(binop '* (const 0) r) (const 0)]
         [(binop '* l (const 0)) (const 0)]
         [(binop '* (const 1) r) r]
         [(binop '* l (const 1)) l]
         [else e]))]))



(define x^3
  (binop '* (variable)
         (binop '* (variable)
                (variable))))

x^3
(define xd (∂ x^3))
xd
(simpl xd)