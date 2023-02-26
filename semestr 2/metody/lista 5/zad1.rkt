#lang racket

;1 - copy
(define (copy xs)
  (if (null? xs)
      null
      (cons (car xs) (copy (cdr xs)))))

;2 - tails
(define (tails xs)
  (if (null? xs)
      (cons null null)
      (cons xs (tails (cdr xs)))))

;3 - reverse
(define (reverse-it xs)
  (define (iter xs acc)
    (if (null? xs)
        acc
        (iter (cdr xs) (cons (car xs) acc))))
  (iter xs null))

;4 - map
(define (map f xs)
  (if (null? xs)
      null
      (cons (f (car xs)) (map f (cdr xs)))))

;5 - zip
(define (zip xs ys)
  (if (null? xs)
      null
      (cons (cons (car xs) (car ys))
            (zip (cdr xs) (cdr ys)))))