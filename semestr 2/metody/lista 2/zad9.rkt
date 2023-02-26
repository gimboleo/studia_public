#lang racket

(define (repeated p n)
  (if (<= n 0)
      p
      (lambda (x)
        ((repeated p (- n 1))
         (p x)))))

(define (repeated-build k n d b)
  ((repeated (lambda (x) (/ n (+ d x))) (- k 1)) b))

(repeated-build 1 1 1 0.0)
(repeated-build 2 1 1 0.0)
(repeated-build 3 1 1 0.0)