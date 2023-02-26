#lang racket

(define (identity x) x)
(define (inc x) (+ x 1))


(define (product val next a b)
  (if (> a b)
      1
      (* (val a) (product val next (next a) b))))

(define (product-iter val next a b)
  (define (iter a res)
    (if (> a b)
        res
        (iter (next a) (* res (val a)))))
  (iter a 1))


(define (factorial a b) (product identity inc a b))
(factorial 1 5)

(define (factorial-iter a b) (product-iter identity inc a b))
(factorial-iter 1 5)

(define (pi-val a)
  (* (/ (* 2 a) (- (* 2 a) 1))
     (/ (* 2 a) (+ (* 2 a) 1))))

(define pi (* (product pi-val inc 1.0 10000) 2))

pi