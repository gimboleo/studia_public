#lang racket

(define (cont-frac num den k)
  (define (frac i)
    (if (< k i)
        0
        (/ (num i) (+ (den i) (frac (+ i 1))))))
  (frac 1))

(define (cont-frac-iter num den k)
  (define (frac-iter i res)
    (if (<= i 0)
        res
        (frac-iter (- i 1) (/ (num i) (+ (den i) res)))))
  (frac-iter k 0))


(cont-frac (lambda (i) 1.0) (lambda (i) 1.0) 10000)
(cont-frac-iter (lambda (i) 1.0) (lambda (i) 1.0) 10000)