#lang racket

(provide cube-root)

(define (cube-root x)
  
  (define (cube-iter y)
    (if (good-enough? y)
        y
        (cube-iter (improve y))))

  (define (good-enough? y)
    (< (abs (- (* y y y) x)) 0.00001))

  (define (improve y)
    (/ (+
        (/ x (* y y))
        (* 2 y))
       3))

  (if (= x 0)
      0
      (cube-iter 1.0)))



(cube-root 27)   ;3
(cube-root 1)    ;1
(cube-root 2)    ;approx. 1.259
(cube-root 4)    ;approx. 1.587
(cube-root 1025) ;approx. 10.082
(cube-root 4758) ;approx. 16.819
(cube-root -11)  ;approx. -2.223
(cube-root 0)    ;0