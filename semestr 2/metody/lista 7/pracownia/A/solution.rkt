#lang racket

(provide (struct-out const) (struct-out binop) (struct-out var-expr) (struct-out let-expr) (struct-out pos) (struct-out var-free) (struct-out var-bound) annotate-expression)

;; ---------------
;; Jezyk wejsciowy
;; ---------------

(struct pos (file line col)     #:transparent)
  
(struct const    (val)          #:transparent)
(struct binop    (op l r)       #:transparent)
(struct var-expr (id)           #:transparent)
(struct let-expr (loc id e1 e2) #:transparent)

(define (expr? e)
  (match e
    [(const n)      (number? n)]
    [(binop op l r) (and (symbol? op) (expr? l) (expr? r))]
    [(var-expr x)   (symbol? x)]
    [(let-expr loc x e1 e2)
     (and (pos? loc) (symbol? x) (expr? e1) (expr? e2))]
    [_ false]))

(define (make-pos s)
  (pos (syntax-source s)
       (syntax-line   s)
       (syntax-column s)))

(define (parse e)
  (let ([r (syntax-e e)])
    (cond
      [(number? r) (const r)]
      [(symbol? r) (var-expr r)]
      [(and (list? r) (= 3 (length r)))
       (match (syntax-e (car r))
         ['let (let* ([e-def (syntax-e (second r))]
                      [x     (syntax-e (first e-def))])
                 (let-expr (make-pos (first e-def))
                           (if (symbol? x) x (error "parse error!"))
                           (parse (second e-def))
                           (parse (third r))))]
         [op   (binop op (parse (second r)) (parse (third r)))])]
      [else (error "parse error!")])))

;; ---------------
;; Jezyk wyjsciowy
;; ---------------

(struct var-free  (id)     #:transparent)
(struct var-bound (pos id) #:transparent)

(define (expr-annot? e)
  (match e
    [(const n)         (number? n)]
    [(binop op l r)    (and (symbol? op) (expr-annot? l) (expr-annot? r))]
    [(var-free x)      (symbol? x)]
    [(var-bound loc x) (and (pos? loc) (symbol? x))]
    [(let-expr loc x e1 e2)
     (and (pos? loc) (symbol? x) (expr-annot? e1) (expr-annot? e2))]
    [_ false]))



(struct environ (xs))

(define env-empty (environ null))

(define (env-add x v loc env)
  (environ (cons (cons x (cons v loc)) (environ-xs env))))

(define (env-lookup x env)
  (define (assoc-lookup xs)
    (cond [(null? xs) #f]
          [(eq? x (car (car xs))) (cdr (car xs))]
          [else (assoc-lookup (cdr xs))]))
  (assoc-lookup (environ-xs env)))


(define (annotate-expression e)
  (define (aux e env)
    (match e
      [(const n) e]
      [(binop op l r) (binop op (aux l env) (aux r env))]
      [(var-expr x) (let ([v (env-lookup x env)])
                      (if (not v)
                          (var-free x)
                          (var-bound (cdr v) x)))]
      [(let-expr loc x e1 e2)
       (let ([v (aux e1 env)])
         (let-expr loc x v (aux e2 (env-add x v loc env))))]))
  (aux e env-empty))


;; Nie uzylem rackunit, poniewaz wynik procedury jest zalezny od lokalizacji pliku na dysku
;; Nie mialem pomyslu jak to sensownie rozwiazac i wydaje mi sie, ze w tym przypadku dosyc latwo zauwazyc czy wynik jest prawidlowy golym okiem

(annotate-expression (parse #'(let [x 5] (* y x))))
(display "\n")
(annotate-expression (parse #'(let [y (+ x y)] (let [x (+ x y)] (+ x y)))))
(display "\n")
(annotate-expression (parse #'(let [x 1] (+ x (let [x 1] (let [x 1] x))))))
(display "\n")
(annotate-expression (parse #'(let [x x] (* (let [y 1] (/ (+ x z) y)) y))))
(display "\n")