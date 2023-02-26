#lang racket

(define (mult a b)
   (if (= b 0)
       0
       (+ a (mult a (- b 1)))))

;(mult a b) ≡ (* a b).
;
;Podstawa indukcji:
;(mult a 0) ≡ 0 ≡ (* a 0) 
;
;Krok indukcyjny:
;Założenie: (mult a n) ≡ (* a n)
;Teza: (mult a (inc n)) ≡ (* a (inc n))
;
;(mult a (inc n)) ≡
;(+ a (mult a n)) ≡
;(+ a (* a n) ≡
;(* a (inc n))