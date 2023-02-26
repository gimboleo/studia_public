#lang racket

(define (accumulate combiner null-value val next a b)
  (if (> a b)
      null-value
      (combiner (val a) (accumulate combiner null-value val next (next a) b))))

(define (accumulate-iter combiner null-value val next a b)
  (define (iter a res)
    (if (> a b)
        res
        (iter (next a) (combiner res (val a)))))
  (iter a null-value))


(define (pi-val a) (/ 1.0 (* a (+ a 2))))
(define (pi-next a) (+ a 4))
(define pi (* (accumulate + 0 pi-val pi-next 1 100000) 8))
pi


;Żeby wynik akumulacji nie zależał od wyboru definicji, combiner musi być operacją łączną i przemienną, a null-value być jej elementem neutralnym.
