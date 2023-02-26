#lang racket

(require rackunit)
(provide caesar)

(define (rotate-left n xs)
  (define m (modulo n (length xs)))
  (append (drop xs m) (take xs m)))

(define (zip xs ys)
  (if (null? xs)
      null
      (cons (cons (car xs) (car ys))
            (zip (cdr xs) (cdr ys)))))


(define (caesar alphabet key)
  (define (aux x m)
    (if (eq? x (caar m))
        (cdar m)
        (aux x (cdr m))))
  
  (define (encode x)
    (define new-alphabet (rotate-left key alphabet))
    (define caesar-map (zip alphabet new-alphabet))
    (aux x caesar-map))

  (define (decode x)
    (define new-alphabet (rotate-left (* -1 key) alphabet))
    (define caesar-map (zip alphabet new-alphabet))
    (aux x caesar-map))

  (cons encode decode))



(define a-z (string->list "abcdefghijklmnopqrstuvwxyz"))
(define ring (caesar a-z 1))
(check-equal? (list->string (map (car ring) (string->list "abcxyz"))) "bcdyza")
(check-equal? (list->string (map (cdr ring) (string->list "bcdyza"))) "abcxyz")

(define test (caesar (list 0 1 2 'a 'b 'c) 2))
(check-equal? (map (car test) (list 0 2 'c 'c 1 2 'b 'a)) (list 2 'b 1 1 'a 'b 0 'c))
(check-equal? (map (cdr test) (list 2 'b 1 1 'a 'b 0 'c)) (list 0 2 'c 'c 1 2 'b 'a))

(define test2 (caesar (list 0 1 2 'a 'b 'c) 6))
(check-equal? (map (car test2) (list 0 2 'c 'c 1 2 'b 'a)) (list 0 2 'c 'c 1 2 'b 'a))
(check-equal? (map (cdr test2) (list 0 2 'c 'c 1 2 'b 'a)) (list 0 2 'c 'c 1 2 'b 'a))