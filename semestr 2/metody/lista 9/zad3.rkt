#lang racket

(struct bdlist (v [prev #:mutable] [next #:mutable]) #:transparent)


(define (list->bdlist xs)
  (define (aux xs prev)
    (if (null? (cdr xs))
        (bdlist (car xs) prev null)
        (let ([bxs (bdlist (car xs) prev null)])
          (set-bdlist-next! bxs (aux (cdr xs) bxs))
          bxs)))
  
  (if (null? xs)
      null
      (let ([bxs (bdlist (car xs) null null)])
        (set-bdlist-next! bxs (aux (cdr xs) bxs))
        bxs)))


(define (bdfilter pred bxs)
  (define (aux prev bys)
    (match bys
      [(bdlist v p n)
       (let ([curr (bdlist v prev null)])
         (if (pred v)
             (let ([rest (aux curr (bdlist-next bys))])
               (begin (set-bdlist-next! curr rest)
                      curr))
             (aux prev (bdlist-next bys))))]
      [null null]))
  (aux null bxs))
                

(define (cycle-bdlist! bxs)
  (define (aux bys)
    (if (null? (bdlist-next bys))
        (begin (set-bdlist-next! bys bxs)
               (set-bdlist-prev! bxs bys))
        (aux (bdlist-next bys))))

  (if (null? bxs)
      null
      (begin (aux bxs)
             bxs)))


(define (decycle-bdlist! bxs)
  (set-bdlist-next! (bdlist-prev bxs) null)
  (set-bdlist-prev! bxs null)
  bxs)


(define x (list->bdlist (list 1 2 3 4)))
x
(cycle-bdlist! x)
(decycle-bdlist! x)