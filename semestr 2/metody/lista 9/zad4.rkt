#lang racket

;; Składnia abstrakcyjna naszego języka
(struct const       (val)           #:transparent)
(struct let-expr    (id val expr)   #:transparent)
(struct letrec-expr (id e1 e2)      #:transparent)
(struct var-expr    (id)            #:transparent)
(struct if-expr     (eb et ef)      #:transparent)
(struct fun         (id expr)       #:transparent)
(struct app         (fun arg)       #:transparent)
(struct quote-expr  (q)             #:transparent) ;; zmiana

;; Symbole zarezerwowane (nie mogą być nazwami zmiennych)
(define (reserved? s)                              ;; zmiana
  (or (member s '(let letrec if lambda true false and or quote quit)))) ; quit zarezerwowane dla repla

;; Dobre nazwy zmiennych: symbole niezarezerwowane
(define (name? s)
  (and (symbol? s)
       (not (reserved? s))))

(define (expr? e)
  (match e
    [(const v) (or (number? v) (boolean? v))]
    [(quote-expr q) true] ;; zmiana
    [(let-expr x e1 e2)
     (and (name? x)  ;; reprezentujemy nazwy zmiennych jako symbole
          (expr? e1)
          (expr? e2))] ;; x jest związany w e2 (ale nie w e1)
    [(letrec-expr x e1 e2)
     (and (name? x)
          (expr? e1)
          (expr? e2))] ;; x jest związany zarówno w e2 jak i w e1
    [(var-expr x) (symbol? x)]
    [(if-expr eb et ef)
     (and (expr? eb)
          (expr? et)
          (expr? ef))]
    [(fun x e)
     (and (symbol? x)
          (expr? e))] ;; x jest związany w e
    [(app e1 e2)
     (and (expr? e1)
          (expr? e2))]
    ;; w predykatach trzeba pamiętać o przypadku domyślnym!
    [_ false]))

;; Obsługa błędów
(struct parse-error (expr))
(struct unbound-var (id))
(struct eval-error  (cause))
(struct type-error  (expected given))

;; Wartości

(struct clo (id body env))
(struct builtin (proc))
(struct quot (q)          #:transparent) ;; zmiana

;; W modelu podstawieniowym wartością funkcji jest ona sama
;; W modelu środowiskowym nie jest tak prosto, bo nie podstawiamy
(define (value? e)
  (or (number?  e)
      (boolean? e)
      (quot?    e) ;; zmiana
      (symbol?  e) ;; zmiana
      (clo?     e)
      (builtin? e)
      (and (pair? e)
           (value? (car e))    ; wartość, bo język jest gorliwy
           (value? (cdr e)))))

(define (chckTyp typ e)
  (if (match typ
        ('quote     (quot?   e)) ;; zmiana
        ('symbol    (symbol? e)) ;; zmiana
        ('number    (number? e))
        ('boolean   (boolean? e))
        ('procedure (or (clo? e) (builtin? e)))
        ('pair      (pair? e)))
      e
      (raise (type-error typ e))))

(define (mk-unop typ proc)
  (builtin
   (lambda (v)
     (chckTyp typ v)
     (proc v))))

(define (mk-binop t1 t2 proc)
  (builtin
   (lambda (x)
     (chckTyp t1 x)
     (builtin
      (lambda (y)
        (chckTyp t2 y)
        (proc x y))))))

(define builtins '(eq? quote? symbol? number? boolean? procedure? pair? + - * / = < > pair fst snd not)) ;; zmiana

(define (op->builtin op)
  (match op
    ('eq?        (builtin (lambda (x)
                            (builtin (lambda (y)
                                       (eq? x y))))))
    ('quote?     (builtin quot?))   ;; zmiana
    ('symbol?    (builtin symbol?)) ;; zmiana
    ('number?    (builtin number?))
    ('boolean?   (builtin boolean?))
    ('procedure? (builtin (lambda (x) (or (clo? x) (builtin? x)))))
    ('pair?      (builtin pair?))
    ('+ (mk-binop 'number 'number +))
    ('- (mk-binop 'number 'number -))
    ('* (mk-binop 'number 'number *))
    ('/ (mk-binop 'number 'number
                  (lambda (x y) (if (= y 0) (raise (eval-error "Division by zero")) (/ x y)))))
    ('= (mk-binop 'number 'number =))
    ('< (mk-binop 'number 'number <))
    ('> (mk-binop 'number 'number >))
    ('pair (builtin (lambda (x) (builtin (lambda (y) (cons x y))))))
    ('fst  (mk-unop 'pair car))
    ('snd  (mk-unop 'pair cdr))
    ('not  (mk-unop 'boolean not))))


(struct not-found ())
(struct blackhole ())
(struct env (assoc))
(define env-empty (env null))

(define (env-lookup ρ x)
  (define (assoc bs)
    (cond
      [(null? bs)               (not-found)]
      [(eq? (mcar (car bs)) x)  (mcdr (car bs))]
      [else                     (assoc (cdr bs))]))
  (assoc (env-assoc ρ)))

(define (env-add ρ x v)
  (env (cons (mcons x v) (env-assoc ρ))))

(define (env-update! ρ x v)
  (define (upd bs)
    (cond
      [(null? bs)               (error "Impossible happened!")]
      [(eq? (mcar (car bs)) x)  (set-mcdr! (car bs) v)]
      [else                     (upd (cdr bs))]))
  (upd (env-assoc ρ)))

(define start-env
  (foldr (lambda (x ρ) (env-add ρ x (op->builtin x))) env-empty builtins))

;; jeśli (expr? e) (env? ρ), to (value? (eval-env e ρ)) (lub błąd)
;; nie doliczymy się do błędu undefined identifier
;; jeśli zmienne wolne e są określone w ρ
(define (eval-env e ρ)
  (match e
    [(const n) n]
    [(var-expr x)
     (match (env-lookup ρ x)
       [(not-found)    (raise (unbound-var x))]
       [(blackhole)    (raise (eval-error "Stuck in a black hole!"))]
       [v              v])]
    [(fun x e)    (clo x e ρ)]
    [(app e1 e2)
     (let* ((v1 (eval-env e1 ρ))
            (v2 (eval-env e2 ρ)))
       (match v1
         [(clo x e ρ) (eval-env e (env-add ρ x v2))]
         [(builtin p) (p v2)]
         [else        (raise (type-error 'procedure v1))]))]
    [(if-expr eb et ef)
     (let ((vb (eval-env eb ρ)))
       (cond
         [(eq? vb true)  (eval-env et ρ)]
         [(eq? vb false) (eval-env ef ρ)]
         [else           (raise (type-error 'boolean vb))]))]
    [(let-expr x e1 e2)
     (let ((v (eval-env e1 ρ)))
       (eval-env e2 (env-add ρ x v)))]
    [(letrec-expr x e1 e2)
     (let* ((ρ (env-add ρ x (blackhole)))
            (v (eval-env e1 ρ)))
       (env-update! ρ x v)
       (eval-env e2 ρ))]
    [(quote-expr q) (if (list? q) (quot q) q)])) ;; zmiana

;; zakładamy że (expr? e), wtedy (value? (eval e)) (lub błąd wykonania)
(define (eval e)
  (eval-env e start-env)) ;; procedury wbudowane lądują w środowisku początkowym

;; (let (x e1) e2) == ((lambda (x) e2) e1)
;; e1 -> v1, potem podstaw v1 za x w e2 i oblicz to wyrażenie

;;;; Parser

(define (tagged-tuple? tag len tup)
  (and (list? tup)
       (pair? tup)
       (eq? tag (car tup))
       (= len (length (cdr tup)))))

(define (make-fun ids e)
  (if (null? ids)
      e
      (fun (car ids) (make-fun (cdr ids) e))))

(define (make-app e es)
  (if (null? es)
      e
      (make-app (app e (car es)) (cdr es))))

;; Chcielibyśmy żeby nasz parser przyjmował zacytowane wyrażenia
;; np. '(+ 2 (* 3 5)) -> 2+3*5
;; (let (x e1) e2) <- składnia konkretna dla let-wyrażeń
;; (let (x 3) (+ x x))
;; (pair 3 2) <- składnia konkretna dla par
;; (lambda (x y z) (+ (+ x y) z)) -> (fun x (fun y (fun z ...)))
;; (e1 e2 e3 e4) -> (app (app (app e1 e2) e3) e4)
(define (parse e)
  (cond
    [(number? e)    (const e)]
    [(eq? e 'true)  (const true)]
    [(eq? e 'false) (const false)]
    [(name? e)      (var-expr e)]
    [(and (list? e)
          (= 3 (length e))
          (eq? 'let (car e))
          (list? (cadr e))
          (= 2 (length (cadr e)))
          (name? (car (cadr e))))
     (let-expr (caadr e) (parse (cadr (cadr e))) (parse (caddr e)))]
    [(and (list? e)
          (= 3 (length e))
          (eq? 'letrec (car e))
          (list? (cadr e))
          (= 2 (length (cadr e)))
          (name? (car (cadr e))))
     (letrec-expr (caadr e) (parse (cadr (cadr e))) (parse (caddr e)))]
    [(and (list? e)
          (= 4 (length e))
          (eq? 'if (first e)))
     (if-expr (parse (second e)) (parse (third e)) (parse (fourth e)))]
    [(and (list? e)
          (= 3 (length e))
          (eq? 'lambda (first e))
          (list? (second e))
          (pair? (second e))
          (andmap name? (second e)))
     (make-fun (second e) (parse (third e)))]
    [(and (list? e)
          (= 3 (length e))
          (eq? (car e) 'and))
     (if-expr (parse (cadr e)) (parse (caddr e)) (const false))]
    [(and (list? e)
          (= 3 (length e))
          (eq? (car e) 'or))
     (if-expr (parse (cadr e)) (const true)  (parse (caddr e)))]
    [(and (list? e) ;; zmiana
          (= 2 (length e))
          (or (eq? (car e) 'quote)
              (eq? (car e) '\')))
     (quote-expr (cadr e))]
    [(and (list? e)
          (> (length e) 1))
     (make-app (parse (car e)) (map parse (cdr e)))]
    [else (raise (parse-error e))]))

;;; Przykład: program liczący silnię (w składni konkretnej)
;;; kwazicytowanie użyte żeby można było łatwo wstawić różne argumenty.

(define (fact-prog n)
  `(letrec (fact (lambda (x)
                   (if (= x 0)
                       1
                       (* x (fact (- x 1))))))
     (fact ,n)))

(define (map-prog f xs)
  `(letrec (map (lambda (f)
                  (lambda (xs)
                    (if (null? xs)
                        null
                        (pair (f (fst xs)) (map f (snd xs)))))))
     (map ,f ,xs)))

(define (filter-prog pred xs)
  `(letrec (filter (lambda (p)
                     (lambda (xs)
                       (if (null? xs)
                           null
                           (if (p (fst xs))
                               (pair (fst xs) (filter p (snd xs)))
                               (filter p (snd xs)))))))
     (filter ,pred ,xs)))

(define (append-prog xs ys)
  `(letrec (append (lambda (xs)
                     (lambda (ys)
                       (if (null? xs)
                           ys
                           (pair (fst xs) (append (snd xs) ys))))))
     (append ,xs ,ys)))

;;;; REPL

;; Prosta pętla czytająca, parsująca i wykonująca programy,
;; i wyświetlająca ich wartości (lub komunikaty o błędach).
;; Polecenie 'quit' kończy działanie ewaluatora.
(define (repl)
  (define (disp-pe pe)
    (display "Parse error: ")
    (displayln (parse-error-expr pe))
    (go))
  (define (disp-te te)
    (display "Type error! Expected: ")
    (display (type-error-expected te))
    (display ",
but given: ")
    (displayln (type-error-given te))
    (go))
  (define (disp-uv uv)
    (display "Unbound variable: ")
    (displayln (unbound-var-id uv))
    (go))
  (define (disp-ee ee)
    (display "Runtime error: ")
    (displayln (eval-error-cause ee))
    (go))
  (define (go)
    (with-handlers
        ([parse-error? disp-pe]
         [type-error?  disp-te]
         [unbound-var? disp-uv]
         [eval-error?  disp-ee])
      (display "> ")
      (let ((text (read)))
        (unless (or (eof-object? text) (eq? text 'quit))
          (let* ((prog (parse text))
                 (val  (eval prog)))
            (displayln val)
            (go))))))
  (go))