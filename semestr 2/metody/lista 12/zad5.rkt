#lang plait

; wyrażenia

(define-type ArithExpr
  (const [val : Number])
  (binop [op : Symbol] [l : ArithExpr] [r : ArithExpr])
  (var-expr [id : Symbol])
  (let-expr [id : Symbol] [e1 : ArithExpr] [e2 : ArithExpr]))

(define (binary-operator? op)
  (member op '(+ - * /)))

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
         [(and (= (length ql) 3)
               (binary-operator? (s-exp->symbol (first ql))))
          (binop (s-exp->symbol (first ql))
                 (parse (second ql))
                 (parse (third ql)))]))]))

; podstawienie

(define (subst e1 x e2)
  (type-case ArithExpr e2
    [(const n)(const n)]
    [(var-expr y)(if (eq? x y) e1 (var-expr y))]
    [(binop op l r)(binop op (subst e1 x l) (subst e1 x r))]
    [(let-expr y e3 e4)
     (let-expr y (subst e1 x e3)
               (if (eq? x y)
                   e4
                   (subst e1 x e4)))]))

; ewaluacja

(define (op->proc op)
  (case op ['+ +] ['- -] ['* *] ['/ /]))

(define (eval e)
  (type-case ArithExpr e
    [(const n) n]
    [(binop op l r) ((op->proc op) (eval l) (eval r))]
    [(let-expr x e1 e2)
     (eval (subst (const (eval e1)) x e2))]
    [(var-expr x)(error x "Unbound variable")]))

(parse `(let [y (+ x 1)] (let [x (+ x y)] (+ y x))))
(display "\n")
(subst (parse `(+ 2 2))
       'x
       (parse `(let [y (+ x 1)] (let [x (+ x y)] (+ y x)))))
(display "\n")
(eval (subst (parse `(+ 2 2))
             'x
             (parse `(let [y (+ x 1)] (let [x (+ x y)] (+ y x))))))
(display "\n")
(parse `x)
(eval (parse `x))