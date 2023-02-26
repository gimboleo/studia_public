#lang racket

(provide integral)

(define (sum val next a b)
  (if (> a b)
      0.0
      (+ (val a) (sum val next (next a) b))))



(define (integral f prec)
  (lambda (a b)

    (define width (/ (- b a) prec))
    
    (define (val-integral a)
      (* (f a) width))
    
    (define (next-integral a)
      (+ a width))
    
    (sum val-integral next-integral a (- b width))))



(define foo (integral (lambda (x) 10) 1000))
(foo 0 10) ;~100

(define foo1 (integral (lambda (x) x) 1000))
(foo1 9 10) ;~9.5
(foo1 0 10) ;~50

(define foo2 (integral sin 1000))
(foo2 0 (* pi 2)) ;~0
(foo2 0 (/ pi 2)) ;~1

((integral tan 1000) (/ pi -2) (/ pi 2)) ;~0
;Ta metoda dla funkcji tan jest niesatysfakcjonująca z powodu antysymetryczności tej metody.
;Przedział całkowania dzielimy na prostokąty od lewej, więc w tym przypadku prostokąty z ujemnej części przedziału są większe od tych z prawej.
;Dodatkowo funkcja dla -pi/2 dąży do -inf, a dla pi/2 do +inf, co prowadzi do bardzo dużego błędu w obliczeniach.

((integral sin 1000) (/ pi -2) (/ pi 2)) ;~0

((integral cos 1000) (/ pi -2) (/ pi 2)) ;~2

((integral (lambda (x) (* x x)) 1000) -1 5) ;~42
((integral (lambda (x) (* x x)) 1000) -10 10) ;~666.(6)

((integral (lambda (x) (* x x x)) 1000) -10 10) ;0
;Anaogiczna sytuacja jak w przypadku funkcji tan. 
