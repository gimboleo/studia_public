#lang racket

(define (permutations xs)
  (define (p-max l xs)
    (define (insert n x xs)
      (define (insert-to nr xs) (if (= nr n) (cons x xs) (cons (car xs) (insert-to (+ nr 1) (cdr xs)))))
      (if (null? xs)
          null
          (if (= n l)
              (cons (insert-to 1 (car xs)) (insert 1 x (cdr xs)))
              (cons (insert-to 1 (car xs)) (insert (+ n 1) x xs)))))
    (cond [(= l 0) null]
          [(= l 1) (list (list (car xs)))]
          [else (insert 1 (car xs) (p-max (- l 1) (cdr xs)))]))
  (p-max (length xs) xs))

(permutations (list 2 3))
(permutations (list 1 2 3))