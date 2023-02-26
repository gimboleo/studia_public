#lang racket

(require rackunit)
(provide null null? cons pair? car cdr)


(define null 'null)

(define (null? x) (eq? x 'null))

(define (cons x y)
  (lambda (a) (cond [(= a 0) x]
                    [(= a 1) y])))

(define (pair? x) (procedure? x))

(define (car x) (x 0))

(define (cdr x) (x 1))


(define (list-sum xs)
  (if (null? xs)
     0
     (+ (car xs)
        (list-sum (cdr xs)))))

(define (length xs)
  (if (null? xs)
      0
      (+ 1 (length (cdr xs)))))

(define (nth n xs)
  (if (= n 0)
      (car xs)
      (nth (- n 1) (cdr xs))))

(define (last xs)
  (if (null? (cdr xs))
      (car xs)
      (last (cdr xs))))


(check-true (pair? (cons 2 3)))
(check-false (pair? null))
(check-true (null? null))
(check-false (null? (cons 2 3)))
(check-false (null? true))
(check-false (pair? 4))


(define lista (cons 2 (cons 3 (cons 5 (cons 9 (cons 15 null))))))
(check-equal? (list-sum lista) 34)
(check-equal? (length lista) 5)
(check-equal? (nth 3 lista) 9)
(check-equal? (last lista) 15)