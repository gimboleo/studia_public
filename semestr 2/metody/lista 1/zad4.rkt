#lang racket
(define (sum-square x y z)
  (define m (min x y z))
  (- (+ (* x x) (* y y) (* z z)) (* m m)))

