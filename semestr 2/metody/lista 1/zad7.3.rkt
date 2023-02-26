#lang racket
(define (power-close-to b n)
  
  (define (find-e e)
    (define x (expt b e))
    (if (> x n)
        e
        (find-e (+ e 1))))
  
  (define (find-e-2 e)
    (define x (expt b e))
    (if (> x n)
        (+ e 1)
        (find-e-2 (- e 1))))
  
  (if (= b 1)
      1
      (if (xor (>= b 1) (>= n 1))
          (find-e-2 0)
          (find-e 0))))
        
(power-close-to 2 1)
(power-close-to 0.5 10)
   
  