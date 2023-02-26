#lang racket

(define (inc x) (+ x 1))
(define (square x) (* x x))


(define (swap p)
  (cons (cdr p) (car p)))

(define (fun-product f g)
  (lambda (p) (cons
               (f (car p))
               (g (cdr p)))))

(swap (cons 2 5))
((fun-product inc square) (cons 3 5))