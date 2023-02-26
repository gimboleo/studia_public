#lang plait

; wyrażenia

(define-type ArithExpr
  (const [val : Number])
  (binop [op : Symbol] [l : ArithExpr] [r : ArithExpr])
  (var-expr [id : Symbol])
  (let-expr [id : Symbol] [e1 : ArithExpr] [e2 : ArithExpr])
  (if-expr [eb : ArithExpr] [et : ArithExpr] [ef : ArithExpr]))

(define (binary-operator? op)
  (member op '(+ - * / = < and or)))

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
                 (parse (third ql)))]))]))

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
  (boolean-val [v : Boolean]))

(define (arith-op f)
  (lambda (x y)
    (number-val (f (number-val-v x) (number-val-v y)))))

(define (comp-op f)
  (lambda (x y)
    (boolean-val (f (number-val-v x) (number-val-v y)))))

(define (bool-op f)
  (lambda (x y)
    (boolean-val (f (boolean-val-v x) (boolean-val-v y)))))

(define (op->proc op)
  (case op
    ['+ (arith-op +)]
    ['- (arith-op -)]
    ['* (arith-op *)]
    ['/ (arith-op /)]
    ['= (comp-op =)]
    ['< (comp-op <)]
    ['and (bool-op (lambda (x y) (and x y)))]
    ['or (bool-op (lambda (x y) (or x y)))]))

(define (eval-env e env)
  (type-case ArithExpr e
    [(const n) (number-val n)]
    [(binop op l r) ((op->proc op) (eval-env l env) (eval-env r env))]
    [(var-expr x) (env-lookup x env)]
    [(let-expr x e1 e2) (eval-env e2 (env-add x (eval-env e1 env) env))]
    [(if-expr eb et ef)
     (if (boolean-val-v (eval-env eb env))
         (eval-env et env)
         (eval-env ef env))]))

(define (eval e) (eval-env e env-empty))

;-------------------------------------------------------------- Zadanie zaczyna sie tu

(define (arith-operator? op)
  (member op '(+ - * /)))

(define (comparison-operator? op)
  (member op '(= <)))

(define (logic-operator? op)
  (member op '(and or)))

(define-type Type
  (number-type)
  (boolean-type))

(define-type-alias TypeEnv (Listof (Symbol * (Optionof Type))))

(define type-env-empty : TypeEnv empty)

(define (type-env-lookup x env)
  (type-case TypeEnv env
    [empty (error 'typeenv-lookup (string-append "Unknown identifier" (to-string x)))]
    [(cons p xs)
     (if (eq? (fst p) x)
         (snd p)
         (type-env-lookup x (rest env)))]))

(define (type-env-add x v env) (cons (pair x v) env))

(define (typecheck-env e env): (Optionof Type)
  (type-case ArithExpr e
    [(const n) (some (number-type))]
    [(binop op l r)
     (let ([ln (typecheck-env l env)]
           [rn (typecheck-env r env)])
       (cond
         [(or (none? ln) (none? rn))
          (none)]
         [(and (arith-operator? op)
               (number-type? (some-v ln))
               (number-type? (some-v rn)))
          (some (number-type))]
         [(and (comparison-operator? op)
               (number-type? (some-v ln))
               (number-type? (some-v rn)))
          (some (boolean-type))]
         [(and (logic-operator? op)
               (boolean-type? (some-v ln))
               (boolean-type? (some-v rn)))
          (some (boolean-type))]
         (else (none))))]
    [(var-expr x) (type-env-lookup x env)]
    [(let-expr x e1 e2)
     (let ([ne1 (typecheck-env e1 env)])
       (if (none? ne1)
         (none)
         (typecheck-env e2 (type-env-add x ne1 env))))]
    [(if-expr b t f)
     (let ([nb (typecheck-env b env)])
       (cond
         [(none? nb) (none)]
         [(boolean-type? (some-v nb))
          (let ([nt (typecheck-env t env)]
                [nf (typecheck-env f env)])
            (if (and (not (none? nt)) (equal? nt nf))
                nt
                (none)))]
         [else (none)]))]))

(define (typecheck e) (typecheck-env e type-env-empty))

;Nie udalo mi sie znalezc informacji o testach jednostkowych w plaicie wiec testy sa po prostu wywolaniami

;(equal? (typecheck (parse `(+ 1 2))) (some (number-type)))
;(equal? (typecheck (parse `(if 0 1 2))) (none))
;(equal? (typecheck (parse `(and (= (+ 2 2) (+ 3 5)) (< 1 2)))) (some (boolean-type)))
;(equal? (typecheck (parse `(let (x 5) (+ x 3)))) (some (number-type)))
;(equal? (typecheck (parse `(let (x (+ 2 7)) (let (y (= 2 2)) (if y (< x 0) (< 0 x)))))) (some (boolean-type)))