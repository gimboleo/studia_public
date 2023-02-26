#lang racket

(define (palindrome? xs)
  (equal? (reverse xs) xs))

(define (rotate-left n xs)
  (define m (modulo n (length xs)))
  (append (drop xs m) (take xs m)))


(palindrome? (string->list "kajak"))
(palindrome? (string->list "zakopanenapokaz"))
(palindrome? (string->list "metody"))

(display "\n")

(rotate-left 2 (list 1 2 3 4 5))
(rotate-left 7 (list 1 2 3 4 5))
(rotate-left -2 (list 1 2 3 4 5))
(rotate-left -11 (list 1 2 3 4 5))