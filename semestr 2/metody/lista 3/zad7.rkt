#lang racket

(define (matrix a b c d)
  (cons (cons a b)
        (cons c d)))

(define (matrix-at m x y)
  (if (= x 1)
      (if (= y 1)
          (car (car m))
          (cdr (car m)))
      (if (= y 1)
          (car (cdr m))
          (cdr (cdr m)))))

(define (matrix? m)
  (and (pair? m)
       (pair? (car m))
       (pair? (cdr m))
       (number? (caar m))
       (number? (cadr m))
       (number? (cdar m))
       (number? (cddr m))))


(define (matrix-mult m n)
  (matrix (+ (* (matrix-at m 1 1) (matrix-at n 1 1)) (* (matrix-at m 1 2) (matrix-at n 2 1)))
          (+ (* (matrix-at m 1 1) (matrix-at n 1 2)) (* (matrix-at m 1 2) (matrix-at n 2 2)))
          (+ (* (matrix-at m 2 1) (matrix-at n 1 1)) (* (matrix-at m 2 2) (matrix-at n 2 1)))
          (+ (* (matrix-at m 2 1) (matrix-at n 1 2)) (* (matrix-at m 2 2) (matrix-at n 2 2)))))

(define matrix-id (matrix 1 0 0 1))


(define (matrix-expt m k)
  (define (expt-help x k)
    (cond [(<= k 0) matrix-id]
          [(= k 1) x]
          [else (expt-help (matrix-mult m x) (- k 1))]))
  (expt-help m k))

(define (fib k)
  (define mtr (matrix 1 1 1 0))
  (matrix-at (matrix-expt mtr k) 1 2))


(define x (matrix 1 2 3 4))
(matrix-expt x 0) ;1/0/0/1
(matrix-expt x 1) ;1/2/3/4
(matrix-expt x 2) ;7/10/15/22
(matrix-expt x 3) ;37/54/81/118

(display "\n")

(fib 0)
(fib 1)
(fib 2)
(fib 3)
(fib 4)
(fib 5)