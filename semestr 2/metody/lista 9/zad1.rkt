#lang racket

(define (list->mlist xs)
  (cond [(null? xs) null]
        [else (mcons (car xs) (list->mlist (cdr xs)))]))

(define (mreverse! mxs)
  (define (aux mys)
    (set-mcdr! (mcdr mxs) mxs)
    (set-mcdr! mxs null)
    mys) 
    
  (cond [(null? mxs) mxs]
        [(null? (mcdr mxs)) mxs]
        [else (aux (mreverse! (mcdr mxs)))]))

(mreverse! (list->mlist (list 1 2 3 4)))