#lang racket

(define (square x) (* x x))

(define (repeated p n)
  (if (<= n 0)
      p
      (lambda (x)
        ((repeated p (- n 1))
         (p x)))))

((repeated square 0) 2)  ;f(x)
((repeated square 1) 2)  ;f(f(x))
((repeated square 2) 2)  ;f(f(f(x)))

