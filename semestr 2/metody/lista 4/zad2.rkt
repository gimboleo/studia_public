#lang racket

(define (insert x xs)
  (if (null? xs)
      (cons x null)
      (if (> x (car xs))
          (cons (car xs) (insert x (cdr xs)))
          (cons x xs))))

(define (insertion-sort xs)
  (foldr insert null xs))


(insert 4 (list 0 1 1 5 7))
(insertion-sort (list 1 5 0 7 1 4 1 0))