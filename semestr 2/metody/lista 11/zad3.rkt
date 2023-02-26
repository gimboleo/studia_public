#lang racket

(define/contract (a x y)
  (parametric->/c [a b] (-> a b a))
  x)

(define/contract (b f g x)
  (parametric->/c [a b c] (-> (-> a b c) (-> a b) a c))
  (f x (g x)))

(define/contract (c f g)
  (parametric->/c [a b c] (-> (-> b c) (-> a b) (-> a c)))
  (lambda (x) (f (g x))))

(define/contract (d f)
  (parametric->/c [a] (-> (-> (-> a a) a) a))
  (f (lambda (x) x)))



(a 2 5)
(b (lambda (x y) (+ x y)) (lambda (x) (* x 2)) 5)
((c (lambda (x) (+ x 10)) (lambda (x) (* x 2))) 5)
(d (lambda (x) (x 2)))