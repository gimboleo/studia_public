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

matrix-id
(define x (matrix 2 5 1 -2))
(define y (matrix 3 -1 7 4))
(matrix-mult x y); 41/18/-11/-9
          
          