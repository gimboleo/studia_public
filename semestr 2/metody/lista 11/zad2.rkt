#lang racket

(define/contract (sublists xs)
  (parametric->/c [a] (-> (listof a) (listof (listof a))))
  (if (null? xs)
      (list null)
      (append-map
       (lambda (ys) (cons (cons (car xs) ys) ys))
       (sublists (cdr xs)))))

(define/contract (sublists-2 xs)
  (parametric->/c [a] (-> (listof a) (listof (listof a))))
  (if (null? xs)
      (list null)
      (append-map
       (lambda (ys) (list (cons (car xs) ys) ys))
       (sublists-2 (cdr xs)))))

;(sublists (list 1 2 3))
(sublists-2 (list 1 2 3))