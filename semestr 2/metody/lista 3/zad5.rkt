#lang racket

(define (matrix a b c d)
  (cons (cons a b)
        (cons c d)))

(define (matrix-at m x y)
  (if (= x 1)
      (if (= y 1)
          (car (car m))
          (cdr (car m)))
      (if (= y 1)
          (car (cdr m))
          (cdr (cdr m)))))

(define (matrix? m)
  (and (pair? m)
       (pair? (car m))
       (pair? (cdr m))
       (number? (caar m))
       (number? (cadr m))
       (number? (cdar m))
       (number? (cddr m))))

(define x (matrix 10 20 30 40))
(matrix-at x 2 1)
(matrix? x)