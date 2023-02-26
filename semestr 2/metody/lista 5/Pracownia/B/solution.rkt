#lang racket

(require rackunit)
(require "sudoku-spec.rkt")

(provide
 rows->board board-rows board-columns board-boxes ; Zad A
 partial-solution-ok? solutions)                  ; Zad B



;;  =========
;;  Zadanie A
;;  =========

;; Tworzy planszę z wierszy (listy list znaków z alfabetu)
(define (rows->board xss) xss)

;; Ujawnia listę wierszy (każdy wiersz to lista znaków z alfabetu)
(define (board-rows board) board)

;; Ujawnia listę kolumn (każda kolumna to lista znaków z alfabetu)
(define (board-columns board)
  (apply map list board))

;; Ujawnia listę pudełek (każde pudełko to lista znaków z alfabetu)
(define (board-boxes board)
  (define l (sqrt (length (car board))))
  (define ll (* l l))
  (define (// a b) (floor (/ a b)))

  ;; Tworzy listę złożoną z x pustych list
  (define (null-list x)
    (if (= x 0)
        null
        (cons null (null-list (- x 1)))))

  ;; Dodaje element x na początek n-tej podlisty listy xs
  (define (add-to-nth xs x n)
    (if (= n 0)
        (cons (cons x (car xs)) (cdr xs))
        (cons (car xs) (add-to-nth (cdr xs) x (- n 1)))))

  ;; Tworzy listę pudełek
  (define (assign-to-boxes elements boxes counter)
    (define row (// counter ll))
    (define column (modulo counter ll)) 
    (if (null? elements)
        boxes
        (assign-to-boxes (cdr elements) (add-to-nth boxes (car elements) (+ (* (// row l) l) (// column l))) (+ counter 1))))

  (assign-to-boxes (flatten board) (null-list ll) 0))



;;  =========
;;  Zadanie B
;;  =========

;; Czy dane częsciowe rozwiązanie (elems, rows) jest poprawne?
(define (partial-solution-ok? initial-board elems rows)

  ;; Tworzy częściowo uzupełniony wiersz
  (define (apply-elems n row)
    (if (= n 0)
        elems
        (cons (car row) (apply-elems (- n 1) (cdr row)))))
  
  ;; Tworzy planszę uzupełnioną częściowym rozwiązaniem
  (define (apply-solution initial-board n)
    (if (> n 0)
        (cons (car initial-board) (apply-solution (cdr initial-board) (- n 1)))
        (if (null? elems)
            rows
            (cons (apply-elems (- (length (car initial-board)) (length elems)) (car initial-board)) rows))))

  ;; Oblicza n dla procedury (apply-solution)
  (define (calculate-n)
    (if (null? elems)
        (- (length initial-board) (length rows))
        (- (length initial-board) (length rows) 1)))

  ;; Sprawdza, czy częściowe rozwiązanie nie nadpisało niepustego miejsca
  (define (didnt-overwrite? xs1 xs2)
    (if (null? xs1)
        #t
        (and (or (eq? (car xs1) '_) (ch-eq? (car xs1) (car xs2)))
             (didnt-overwrite? (cdr xs1) (cdr xs2)))))

  ;; Sprawdza, czy lista składa się wyłącznie z unikalnych wartości i _
  (define (is-unique? xs temp)
    (if (null? xs)
        #t
        (if (eq? (car xs) '_)
            (is-unique? (cdr xs) temp)
            (if (memf (lambda (arg) (ch-eq? arg (car xs))) temp)
                #f
                (is-unique? (cdr xs) (cons (car xs) temp))))))

  ;; Wywołuje (is-unique?) dla kazdej podlisty w liscie
  (define (apply-is-unique? xs)
    (if (null? xs)
        #t
        (and (is-unique? (car xs) null) (apply-is-unique? (cdr xs)))))
  
  (define new (apply-solution initial-board (calculate-n)))
  (and (didnt-overwrite? (flatten initial-board) (flatten new))
       (apply-is-unique? (board-rows new))
       (apply-is-unique? (board-columns new))
       (apply-is-unique? (board-boxes new))))

;; Lista poprawnych częściowych wierszy po dodaniu
;; nowego znaku do jakiegoś częściowego rozwiązania
;; (elems, rows)
(define (new-elems initial-board elems rows)
  (filter
   (λ(es) (partial-solution-ok? initial-board es rows))
   (map (λ(c) (cons c elems)) alphabet)))

;; Lista poprawnych wierszy możliwych do dodania do
;; częściowego rozwiązania zawierającego tylko pełne
;; wiersze (rows)
(define (new-rows initial-board rows)
  (map (λ(r) (cons r rows))
       (foldr (λ(_ ess)
                (append-map
                 (λ(es) (new-elems initial-board es rows))
                 ess))
              (list null)
              alphabet)))

;; Lista poprawnych pełnych rozwiązań
(define (solutions initial-board)
  (map (λ(s) (rows->board s))
       (foldr (λ(_ rss)
                (append-map
                 (λ(rs) (new-rows initial-board rs))
                 rss))
              (list null)
              alphabet)))



(check-equal? (board-rows (rows->board '((_ _ 4 _) (_ 3 _ _) (1 2 _ 4) (_ 4 _ _)))) '((_ _ 4 _) (_ 3 _ _) (1 2 _ 4) (_ 4 _ _)))
(check-equal? (board-columns (rows->board '((_ 4 _ _) (1 2 _ 4) (_ 3 _ _) (_ _ 4 _)))) '((_ 1 _ _) (4 2 3 _) (_ _ _ 4) (_ 4 _ _)))
(check-equal? (board-boxes (rows->board '((_ 4 _ _) (1 2 _ 4) (_ 3 _ _) (_ _ 4 _)))) '((2 1 4 _) (4 _ _ _) (_ _ 3 _) (_ 4 _ _)))
(check-equal? (partial-solution-ok? (rows->board '((_ _ 4 _) (_ 3 _ _) (1 2 _ 4) (_ 4 _ _)))
                                    '(2 1)
                                    '((1 2 3 4) (3 4 1 2)))
              #t)