#lang racket

(define (elem x xs)
  (if (null? xs)
      #f
      (or (eq? x (car xs))
          (elem x (cdr xs)))))

(define (elem-foldr x xs)
  (foldr (lambda (a b) (or (eq? a x) b)) #f xs))


(define (filter p xs)
  (if (null? xs)
      null
      (if (p (car xs))
          (cons (car xs) (filter p (cdr xs)))
          (filter p (cdr xs)))))

(define (filter-foldr p xs)
  (foldr
   (lambda (a b) (if (p a) (cons a b) b))
   null
   xs))


(define (maximum xs)
  (define (aux m l)
    (if (null? l) m
        (if (> m (car l))
            (aux m (cdr l))
            (aux (car l) (cdr l)))))
  (if (null? xs) (error 'maximum "pamietaj, cholero, maximum nie dziala z lista dlugosci zero")
      (aux (car xs) (cdr xs))))

(define (maximum-foldr xs)
  (define (aux x m) (if (> x m) x m))
  (if (null? xs) (error 'maximum "pamietaj, cholero, maximum nie dziala z lista dlugosci zero")
      (foldr aux (car xs) (cdr xs))))


(define (zip xs ys)
  (if (null? xs)
      null
      (cons (cons (car xs) (car ys))
            (zip (cdr xs) (cdr ys)))))

(define (zip-foldr xs ys)
  (car (foldr (lambda (a b) (cons (cons (cons a (cadr b))
                                        (car b))
                                  (cddr b)))
              (cons null (reverse ys)) xs)))

;(1 2 3 4) (a b c d)
;() . (d c b a)
;((4 . d)) . (c b a)
;((3 . c) (4 . d)) . (b a)
;((2 . b) (3 . c) (4 . d)) . (a)
;((1 . a) (2 . b) (3 . c) (4 . d)) . ()


(define (every-other xs)
  (if (null? xs)
      null
      (if (null? (cdr xs))
          (cons (car xs) null)
          (cons (car xs) (every-other (cdr (cdr xs)))))))

(define (every-other-foldr xs)
  (car (foldr (lambda (a b) (cons (cons a (cdr b)) (car b)))
              (cons null null)
              xs)))

;(1 5 0 7 1 4 1 0)
;(null . null)
;((0 . null) . null)
;((1 . null) . (0 . null))
;((4 . (0 . null)) . (1 . null))
;((1 . (1 . null)) (4 . (0 . null)))


(define (tails xs)
  (if (null? xs)
      (cons null null)
      (cons xs (tails (cdr xs)))))

(define (tails-foldr xs)
  (foldr (lambda (a b) (cons (cons a (car b)) b)) (cons null null) xs))

;(0 1 2 3)
;(null . null)
;((3 . null) . null)
;((2 . (3 . null)) . (3 . null))
;((1 . (2 . (3 . null))) . ((2 . (3 . null)) . (3 . null)))



(elem #\a (string->list "dobranoc"))
(elem #\a (string->list "dzien dobry"))
(elem-foldr #\a (string->list "dobranoc"))
(elem-foldr #\a (string->list "dzien dobry"))

(display "\n")

(filter odd? (list 1 5 0 7 1 4 1 0))
(filter-foldr odd? (list 1 5 0 7 1 4 1 0))

(display "\n")

(maximum (list 1 5 0 7 1 4 1 0))
(maximum-foldr (list 1 5 0 7 1 4 1 0))

(display "\n")

(zip '(1 2 3 4) (string->list "abcd"))
(zip-foldr '(1 2 3 4) (string->list "abcd"))

(display "\n")

(every-other (list 1 5 0 7 1 4 1 0))
(every-other (list 0 1 5 0 7 1 4 1 0))
(every-other-foldr (list 1 5 0 7 1 4 1 0))
(every-other-foldr (list 0 1 5 0 7 1 4 1 0))

(display "\n")

(tails (list 0 1 2 3))
(map list->string (tails (string->list "metody")))
(tails-foldr (list 0 1 2 3))
(map list->string (tails-foldr (string->list "metody")))