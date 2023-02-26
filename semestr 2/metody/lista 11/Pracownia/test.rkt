#lang racket

(define/contract (with-labels f xs)
  (parametric->/c [a b] (-> (-> a b) (listof a) (listof (cons/c b (cons/c a null?)))))
  (map (lambda (x) (list (f x) x)) xs))

(define/contract (foldr-map f a xs)
  (parametric->/c [a acc c] (-> (-> a acc (cons/c c acc)) acc (listof a) (cons/c (listof c) acc)))
  (define (it a xs ys)
    (if (null? xs)
        (cons ys a)
        (let [(p (f (car xs) a))]
          (it (cdr p)
              (cdr xs)
              (cons (car p) ys)))))
  (it a (reverse xs) null))

(define/contract (pair-from f g)
  (parametric->/c [a b c] (-> (-> a b) (-> a c) (-> a (cons/c b c))))
  (lambda (x) (cons (f x) (g x))))

(with-labels number->string (list 1 2 3))
(foldr-map (lambda (x a) (cons a (+ a x))) 0 '(1 2 3))
((pair-from (lambda (x) (+ x 1)) (lambda (x) (* x 2))) 2)