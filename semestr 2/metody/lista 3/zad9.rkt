#lang racket

(define (matrix a b c d)
  (lambda (x y) (cond [(= x 1) (if (= y 1) a b)]
                      [(= y 1) c]
                      [else d])))

(define (matrix-at m x y) (m x y))

(define (matrix? m) (procedure? m))



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

; Szybkie potęgowanie - rekurencyjnie
(define (fast-matrix-expt-rec m k)
  (cond
    [(= k 0)
     matrix-id]
    [(= (modulo k 2) 1)
     (matrix-mult m (fast-matrix-expt-rec m (- k 1)))]
    [else
     (let ([new-m (fast-matrix-expt-rec m (/ k 2))])
       (matrix-mult new-m new-m))]))

; Szybkie potęgowanie - iteracyjnie
(define (fast-matrix-expt m k)
  (define (iter acc inner i)
    (cond
      [(= i 0)
       acc]
      [(= i 2)
       (matrix-mult acc (matrix-expt inner 2))]
      [(= (modulo i 2) 1)
       (iter (matrix-mult inner acc) inner (- i 1))]
      [else
       (iter acc (matrix-expt inner 2) (/ i 2))]))
  (iter matrix-id m k))

(define (fast-fib k)
  (matrix-at (fast-matrix-expt (matrix 1 1 1 0) k) 1 2))

(define (fast-fib-rec k)
  (matrix-at (fast-matrix-expt-rec (matrix 1 1 1 0) k) 1 2))



(fib 0)
(fast-fib 1)
(fast-fib-rec 2)
(fast-fib-rec 3)
(fast-fib-rec 4)
(fast-fib-rec 5)