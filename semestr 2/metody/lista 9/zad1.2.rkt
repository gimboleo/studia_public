#lang racket

(define (list->mlist xs)
  (cond [(null? xs) null]
        [else (mcons (car xs) (list->mlist (cdr xs)))]))


(define (mreverse curr)
  (define (push prev curr)
    (if (null? curr)
        prev
        (begin
          (let [(v (mcar curr))]
            (set-mcar! curr prev)
            (push v (mcdr curr))))))

  (if (null? curr)
      (void)
      (begin
        (set-mcar! curr (push (mcar curr) (mcdr curr)))
        (mreverse (mcdr curr)))))


(define x (list->mlist (list 1 2 3 4)))
x
(mreverse x)
x