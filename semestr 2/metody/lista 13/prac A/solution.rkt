#lang plait

(define (zip xs ys)
  (if (empty? xs)
      empty
      (cons (pair (first xs) (first ys)) (zip (rest xs) (rest ys)))))

(define (occurs v exp)
  (cond
    [(s-exp-number? exp) #f]
    [(s-exp-boolean? exp) #f]
    [(s-exp-symbol? exp) (equal? v exp)]
    [(s-exp-list? exp) (foldr (lambda (x y) (or (occurs v x) y)) #f (s-exp->list exp))]))

(define-type-alias Subst (Listof (Symbol * S-Exp)))
(define-type-alias Eq (S-Exp * S-Exp))
(define-type-alias Eqs (Listof Eq))

(define (eq-l [eq : Eq]) (fst eq))
(define (eq-r [eq : Eq]) (snd eq))

(define (eqs-single exp1 exp2) : Eqs
  (list (pair exp1 exp2)))

(define (eqs-append eqs1 eqs2) : Eqs
  (append eqs1 eqs2))

(define subst-empty : Subst
  empty)

(define (subst-single v exp) : Subst
  (list (pair v exp)))

(define (subst-lookup s v)
  (type-case Subst s
    [empty (none)]
    [(cons p ps)
     (if (eq? (fst p) v)
         (some (snd p))
         (subst-lookup (rest s) v))]))

(define (substitute-var s v)
  (type-case (Optionof S-Exp) (subst-lookup s v)
  [(none) (symbol->s-exp v)]
  [(some t) t]))

(define (substitute s exp)
  (cond
    [(s-exp-number? exp) exp]
    [(s-exp-boolean? exp) exp]
    [(s-exp-symbol? exp) (substitute-var s (s-exp->symbol exp))]
    [(s-exp-list? exp) (list->s-exp (foldr (lambda (x y) (cons (substitute s x) y)) empty (s-exp->list exp)))]))

(define (substitute-eqs s eqs): Eqs
  (map (lambda (p) (pair (substitute s (eq-l p))
                        (substitute s (eq-r p)))) eqs))

(define (substitute-subst s s2) : Subst
  (map (lambda (p) (pair (fst p) (substitute s (snd p)))) s2))

(define (subst-compose s1 s2) : Subst
  (append s1 (substitute-subst s1 s2)))

(define (unify eqs)
  (local
    [(define (iter s eqs)
       (type-case Eqs eqs
         [empty (some s)]
         [(cons eq eqs1)
          (let ([eql (eq-l eq)]
                [eqr (eq-r eq)])
            (cond
              [(and (s-exp-symbol? eql)
                    (s-exp-symbol? eqr)
                    (equal? eql eqr))
               (iter s eqs1)]
              [(and (s-exp-number? eql)
                    (s-exp-number? eqr)
                    (equal? eql eqr))
               (iter s eqs1)]
              [(and (s-exp-boolean? eql)
                    (s-exp-boolean? eqr)
                    (equal? eql eqr))
               (iter s eqs1)]
              [(and (s-exp-list? eql)
                    (s-exp-list? eqr))
               (let ([l-list (s-exp->list eql)]
                     [r-list (s-exp->list eqr)])
                 (if (= (length l-list) (length r-list))
                     (iter s (eqs-append (zip l-list r-list) eqs1))
                     (none)))]
              [(s-exp-symbol? eql)
               (if (occurs eql eqr)
                   (none)
                   (let ([s1 (subst-single (s-exp->symbol eql) eqr)])
                     (iter (subst-compose s1 s)
                           (substitute-eqs s1 eqs1))))]
              [(s-exp-symbol? eqr)
               (iter s (eqs-append (eqs-single eqr eql) eqs1))]
              [else (none)]))]))]
    (iter subst-empty eqs)))



;(equal? (unify (list (pair `x `1))) (some (list (values 'x `1))))
;(equal? (unify (list (pair `x `1) (pair `y `#t) (pair `(z q) `(x y)))) (some (list (values 'q `#t) (values 'z `1) (values 'y `#t) (values 'x `1))))
;(equal? (unify (list (pair `x `1) (pair `y `#t) (pair `(z z) `(x y)))) (none))
;(equal? (unify (list (pair `x `(y z)) (pair `x `(y z)))) (some (list (values 'x `(y z)))))
;(equal? (unify (list (pair `x `1) (pair `y `(z x)) (pair `y `(t x)) (pair `a `b))) (some (list (values 'a `b) (values 'z `t) (values 'y `(t 1)) (values 'x `1))))