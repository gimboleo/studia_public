#lang racket
(define (power-close-to b n)
  (define (find-e e)
    (define x (expt b e))
    (if (> x n)
        e
        (find-e (+ 1 e))))
  (find-e 0))
        
(power-close-to 2 1000)
      
  