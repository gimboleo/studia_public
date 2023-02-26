#lang racket

; --------- ;
; Wyrazenia ;
; --------- ;

(struct const    (val)      #:transparent)
(struct binop    (op l r)   #:transparent)
(struct var-expr (id)       #:transparent)
(struct let-expr (id e1 e2) #:transparent)

(define (expr? e)
  (match e
    [(const n) (number? n)]
    [(binop op l r) (and (symbol? op) (expr? l) (expr? r))]
    [(var-expr x) (symbol? x)]
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

(define (test-parse) (parse '(let [x (+ 2 2)] (+ x 1))))


;; generating a symbol using a counter

(define (number->symbol i)
  (string->symbol (string-append "x" (number->string i))))
; ---------- ;
; Srodowiska ;
; ---------- ;

(struct environ (xs))

(define env-empty (environ null))
(define (env-add x v env)
  (environ (cons (cons x v) (environ-xs env))))
(define (env-lookup x env)
  (define (assoc-lookup xs)
    (cond [(null? xs) false] ;;zmieniamy env-lookup tak zeby zwracalo false a nie błąd 
          [(eq? x (car (car xs))) (cdr (car xs))]
          [else (assoc-lookup (cdr xs))]))
  (assoc-lookup (environ-xs env)))

; --------- ;
; Ewaluacja ;
; --------- ;

(struct indexed-expr (e i) #:transparent) ; wyrazenie i indeks do generowania nowych zmiennych  

;; zadanie: tak przemianować zmienne, żeby wszystkie były różne

;; Robimy ewaluator, w ktorym zaiast obliczac wyrazenia zwracamy je z
;; podmienionymi zmiennymi.
;; W środowisku pamiętamy oryginalne zmienne związane i ich nowe nazwy
;; dodatkowo pamiętamy pierwszy wolny indeks dla  generowanej zmiennej

(define (eval-env e env i)
  ;; zwracamy strukturę złożoną z wynikowego wyrażenia i aktualnego indeksu
  (match e
    [(const n) (indexed-expr (const n) i)]
    [(binop op l r)
     (let* ((il (eval-env l env i))
            (ir (eval-env r env (indexed-expr-i il))))
       (indexed-expr (binop op
                            (indexed-expr-e il)
                            (indexed-expr-e ir))
                     (indexed-expr-i ir)))]
    [(let-expr x e1 e2)
     (let* ((newx (number->symbol i))
            (ie1  (eval-env e1  env (+ 1 i)))
            (ie2  (eval-env e2
                            (env-add x newx env)
                            (indexed-expr-i ie1))))
       (indexed-expr
        (let-expr newx
                  (indexed-expr-e ie1)
                  (indexed-expr-e ie2))
        (indexed-expr-i ie2)))]
                 
                
                 
    [(var-expr x) (indexed-expr
                   (let ((v (env-lookup x env)))
                     (if v (var-expr v) (var-expr x)))
                   i)]))

(define (rename e) (indexed-expr-e (eval-env e env-empty 1)))

(define ex1 (parse '(let (x 3) (+ x (let (x 5) x))))) 
(define ex2 (parse '(+ (let (x 1) x) (let (x 1) x)))) 

(rename ex1)
(rename ex2)
(rename (binop '+ (let-expr 'x (const 1) (var-expr 'x)) (let-expr 'x (const 1) (var-expr 'x))))
(rename (let-expr 'x (binop '* (const 3) (var-expr 'x)) (binop '+ (var-expr 'x) (let-expr 'x (binop '* (var-expr 'x) (const 5)) (var-expr 'x)))))
(rename (let-expr 'x (const 3) (binop '+ (var-expr 'x) (let-expr 'x (const 5) (var-expr 'x)))))