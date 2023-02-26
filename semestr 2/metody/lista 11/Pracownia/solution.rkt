#lang racket

(provide (contract-out
          [with-labels with-labels/c]
          [foldr-map foldr-map/c]
          [pair-from pair-from/c]))

(provide with-labels/c foldr-map/c pair-from/c)

(require rackunit)



(define with-labels/c (parametric->/c [a b] (-> (-> a b) (listof a) (listof (cons/c b (cons/c a null?))))))
(define (with-labels f xs)
  (map (lambda (x) (list (f x) x)) xs))

(define foldr-map/c (parametric->/c [a acc c] (-> (-> a acc (cons/c c acc)) acc (listof a) (cons/c (listof c) acc))))
(define (foldr-map f a xs)
  (define (it a xs ys)
    (if (null? xs)
        (cons ys a)
        (let [(p (f (car xs) a))]
          (it (cdr p)
              (cdr xs)
              (cons (car p) ys)))))
  (it a (reverse xs) null))

(define pair-from/c (parametric->/c [a b c] (-> (-> a b) (-> a c) (-> a (cons/c b c)))))
(define (pair-from f g)
  (lambda (x) (cons (f x) (g x))))



(check-equal? (with-labels number->string (list 1 2 3)) '(("1" 1) ("2" 2) ("3" 3)))
(check-equal? (foldr-map (lambda (x a) (cons a (+ a x))) 0 '(1 2 3)) '((5 3 0) . 6))
(check-equal? ((pair-from (lambda (x) (+ x 1)) (lambda (x) (* x 2))) 2) '(3 . 4))