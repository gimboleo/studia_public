#lang racket

(define (repeated p n)
  (if (<= n 0)
      (lambda (x) x)
      (lambda (x)
        ((repeated p (- n 1))
         (p x)))))


(define (fib n)
  (define (step p)
    (cons (cdr p)
          (+ (cdr p) (car p))))
  
  (car ((repeated step n) (cons 0 1))))


(define (3-fib n)
  (define (step p)
    (list (second p)
          (third p)
          (+ (first p) (second p) (third p))))
  
  (car ((repeated step n) (list 0 0 1))))


(define (k-fib k n)
  (define (sum-list p)
    (if (null? (cdr p))
        (car p)
        (+ (car p) (sum-list (cdr p)))))
  
  (define (step p)
    (define x (sum-list p))
    (define (step-help p)
      (if (= (length p) 1)
          (cons x null)
          (cons (cadr p) (step-help (cdr p)))))
    (step-help p))
  
  (car ((repeated step n) (append (build-list (- k 1) (lambda (x) 0)) (list 1)))))

    
    
(fib 0)
(fib 1)
(fib 2)
(fib 3)
(fib 4)
(fib 5)

(display "\n")

(3-fib 0)
(3-fib 1)
(3-fib 2)
(3-fib 3)
(3-fib 4)
(3-fib 5)
(3-fib 6)
(3-fib 7)
(3-fib 8)
(3-fib 9)

(display "\n")

(k-fib 4 0)
(k-fib 4 1)
(k-fib 4 2)
(k-fib 4 3)
(k-fib 4 4)
(k-fib 4 5)
(k-fib 4 6)
(k-fib 4 7)
(k-fib 4 8)
(k-fib 4 9)
