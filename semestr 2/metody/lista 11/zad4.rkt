#lang racket

;Zapetla sie ale dziala I guess?

(define/contract (f x)
  (parametric->/c [a b] (-> a b))
  (f x))

(f 5)