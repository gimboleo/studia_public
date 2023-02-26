#lang racket

; kwazicytowanie
;`(+ 2 ,(+ 2 2))

(define (list-prog p)
  `(let (null 0)
     (let (null? (lambda (x) (and (not (pair? x)) (= 0 x))))
       ,p)))

(define (map-prog f xs)
  `(letrec (map (lambda (f)
                  (lambda (xs)
                    (if (null? xs)
                        null
                        (pair (f (fst xs)) (map f (snd xs)))))))
     (map ,f ,xs)))

(define f '(lambda (x) (* x x)))

(define xs '(pair -1 (pair -2 (pair 3 (pair 0 null)))))

;(list-prog (map-prog f xs))

(define (filter-prog pred xs)
  `(letrec (filter (lambda (p)
                     (lambda (xs)
                       (if (null? xs)
                           null
                           (if (p (fst xs))
                               (pair (fst xs) (filter p (snd xs)))
                               (filter p (snd xs)))))))
     (filter ,pred ,xs)))

(define p '(lambda (x) (> x 0)))

;(list-prog (filter-prog p xs))

(define (append-prog xs ys)
  `(letrec (append (lambda (xs)
                     (lambda (ys)
                       (if (null? xs)
                           ys
                           (pair (fst xs) (append (snd xs) ys))))))
     (append ,xs ,ys)))

(eval (parse (list-prog (append-prog xs xs))))
