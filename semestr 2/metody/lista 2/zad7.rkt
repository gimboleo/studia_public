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


(define (num-pi i)
  (define (square x) (* x x))
  (square (- (* 2 i) 1)))

(define (den-pi i) 6.0)

(define pi (+ 3 (cont-frac num-pi den-pi 16)))
(define pi-iter (+ 3 (cont-frac-iter num-pi den-pi 16)))
pi
pi-iter
