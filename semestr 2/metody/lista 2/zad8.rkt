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


(define (atan-cf x k)
  (define (t-num i)
    (define (square x) (* x x))
    (if (= i 1)
        x
        (square (* (- i 1) x))))
  (define (t-den i) (- (* 2 i) 1))
  (cont-frac t-num t-den k))


(atan-cf 2.0 40)
(atan 2)
        