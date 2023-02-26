#lang racket

(define empty-queue (cons null null))

(define (empty? q)
  (and (pair? q) (null? (car q)) (null? (cdr q))))

(define (push-back x q)
  (if (empty? q)
      (cons (list x) null)
      (cons (car q) (cons x (cdr q)))))

(define (front q) (caar q))

(define (pop q)
  (if (null? (cdar q))
      (cons (reverse (cdr q)) null)
      (cons (cdar q) (cdr q))))

(define q empty-queue)
q
(push-back 1 q)
(push-back 2 (push-back 1 q))
(push-back 3 (push-back 2 (push-back 1 q)))
(pop (push-back 3 (push-back 2 (push-back 1 q))))
(pop (pop (push-back 3 (push-back 2 (push-back 1 q)))))
(pop (pop (pop (push-back 3 (push-back 2 (push-back 1 q))))))