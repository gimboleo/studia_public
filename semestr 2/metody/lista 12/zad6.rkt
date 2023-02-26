#lang plait

; wyrażenia

(define-type ArithExpr
  (const [val : Number])
  (binop [op : Symbol] [l : ArithExpr] [r : ArithExpr])
  (unop  [op : Symbol] [v : ArithExpr])  ;; <------ ZADANIE 6 (unop)
  (var-expr [id : Symbol])
  (let-expr [id : Symbol] [e1 : ArithExpr] [e2 : ArithExpr])
  (if-expr [eb : ArithExpr] [et : ArithExpr] [ef : ArithExpr]))

(define (binary-operator? op)
  (member op '(+ - * / = < and or pair)))  ;; <------ ZADANIE 6 (pair)

(define (unary-operator? op)  ;; <------ ZADANIE 6 (unop)
  (member op '(- not fst snd)))  ;; <------ ZADANIE 6 (pair)

(define (parse q)
  (cond
    [(s-exp-number? q) (const (s-exp->number q))]
    [(s-exp-symbol? q) (var-expr (s-exp->symbol q))]
    [(s-exp-list? q)
     (let ([ql (s-exp->list q)])
       (cond
         [(and (= (length ql) 3)
               (equal? (first ql) `let))
          (let ([ll (s-exp->list (second ql))])
            (let-expr (s-exp->symbol (first ll))
                      (parse (second ll))
                      (parse (third ql))))]
         [(and (= (length ql) 4)
               (equal? (first ql) `if))
          (if-expr (parse (second ql))
                   (parse (third ql))
                   (parse (fourth ql)))]
         [(and (= (length ql) 3)
               (binary-operator? (s-exp->symbol (first ql))))
          (binop (s-exp->symbol (first ql))
                 (parse (second ql))
                 (parse (third ql)))]
         [(and (= (length ql) 2)  ;; <------ ZADANIE 6 (unop)
               (unary-operator? (s-exp->symbol (first ql))))
          (unop (s-exp->symbol (first ql))
                (parse (second ql)))]))]))
       

; środowiska

(define-type-alias (Env 'a) (Listof (Symbol * 'a)))

(env-empty : (Env 'a))
(define env-empty empty)

(define (env-add x v env) (cons (pair x v) env))

(define (env-lookup x env)
  (type-case (Env 'a) env
    [empty (error 'env-lookup (string-append "Unknown identifier "
                                             (to-string x)))]
    [(cons p ps)
     (if (eq? (fst p) x)
         (snd p)
         (env-lookup x (rest env)))]))

; ewaluacja

(define-type Value
  (number-val [v : Number])
  (boolean-val [v : Boolean])
  (pair-val [v : (Value * Value)]))  ;; <------ ZADANIE 6 (pair) ;; CHANGED
  

(define (arith-op f)
  (lambda (x y)
    (number-val (f (number-val-v x) (number-val-v y)))))

(define (arith-unop f)  ;; <------ ZADANIE 6 (unop)
  (lambda (x)
    (number-val (f (number-val-v x)))))

(define (comp-op f)
  (lambda (x y)
    (boolean-val (f (number-val-v x) (number-val-v y)))))

(define (bool-op f)
  (lambda (x y)
    (boolean-val (f (boolean-val-v x) (boolean-val-v y)))))

(define (bool-unop f)  ;; <------ ZADANIE 6 (unop)
  (lambda (x)
    (boolean-val (f (boolean-val-v x)))))

(define (get-pair-op f)  ;; <------ ZADANIE 6 (pair)
  (lambda (p)
    (f (pair-val-v p)))) ;; CHANGED

(define (op->proc op)
  (case op
    ['+ (arith-op +)]
    ['- (arith-op -)]
    ['* (arith-op *)]
    ['/ (arith-op /)]
    ['= (comp-op =)]
    ['< (comp-op <)]
    ['and (bool-op (lambda (x y) (and x y)))]
    ['or (bool-op (lambda (x y) (or x y)))]
    ['pair (lambda (x y) (pair-val (pair x y)))]))  ;; <------ ZADANIE 6 (pair)

;; Osobna procedura dla operatorów unarnych,
;; żeby rozróżnić minusa binarnego i unarnego.
(define (unop->proc op)  ;; <------ ZADANIE 6 (unop) 
  (case op
    ['- (arith-unop (lambda (x) (- 0 x)))]
    ['not (bool-unop (lambda (x) (not x)))]
    ['fst (get-pair-op fst)]  ;; <------ ZADANIE 6 (pair)
    ['snd (get-pair-op snd)]))  ;; <------ ZADANIE 6 (pair)

(define (eval-env e env)
  (type-case ArithExpr e
    [(const n) (number-val n)]
    [(binop op l r) ((op->proc op) (eval-env l env) (eval-env r env))]
    [(unop op v) ((unop->proc op) (eval-env v env))]  ;; <------ ZADANIE 6 (unop)
    [(var-expr x) (env-lookup x env)]
    [(let-expr x e1 e2) (eval-env e2 (env-add x (eval-env e1 env) env))]
    [(if-expr eb et ef)
     (if (boolean-val-v (eval-env eb env))
         (eval-env et env)
         (eval-env ef env))]))
    

(define (eval e) (eval-env e env-empty))

(eval (parse `(let [x 5] (if (= x 5) 1 0))))
(eval (parse `(let [x 5] (if (not (= x 5)) 9 (- 3)))))  ;; <------ ZADANIE 6 (unop)
(eval (parse `(let [p (pair (+ 2 1) (- 5))] (* (fst p) (snd p)))))  ;; <------ ZADANIE 6 (pair)
;; Nie działa:  (chyba dziala? xd)
(eval (parse `(pair (pair 1 2) 3)))
(eval (parse `(pair (< 1 0) (< 0 1))))
(eval (parse `(pair (< 0 1) 5)))