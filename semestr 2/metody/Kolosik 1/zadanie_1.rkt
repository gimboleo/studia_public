#lang racket

(define (foldr f i xs)
  (if (null? xs)
      i
      (f (car xs)
         (foldr f i (cdr xs)))))

(define (kwadraty-liczb-parzystych xs)
  (define (square x) (* x x))
  (foldr (lambda (a b) (if (even? a) (cons (square a) b) b))
         null
         xs))

(define (aplikuj-procedury fs x)
  (foldr (lambda (a b) (a b)) x fs))

(define (wstaw-pomiedzy x xs)
  (foldr (lambda (a b) (cons x (cons a b))) (list x) xs))

(define (grupuj xs)
  (group-by identity xs))