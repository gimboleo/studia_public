#lang racket

(define leaf 'leaf)
(define (leaf? t) (eq? t 'leaf))

(define (node v l r) (list 'node v l r))
(define (node? t)
  (and (list? t)
       (= (length t) 4)
       (eq? (first t) 'node)))

(define (node-val t) (second t))
(define (node-left t) (third t))
(define (node-right t) (fourth t))

(define (tree? t)
  (or (leaf? t)
      (and (node? t)
           (tree? (node-left t))
           (tree? (node-right t)))))


(define (sum-paths tt)
  (define (aux acc tt)
    (if (leaf? tt)
        leaf
        (node (+ (node-val tt) acc)
              (aux (+ (node-val tt) acc) (node-left tt))
              (aux (+ (node-val tt) acc) (node-right tt)))))
  (aux 0 tt))


(define tt
  (node 1 (node 2 (node 3 leaf leaf)
                (node 30 leaf leaf))
        (node 9 (node 2 leaf leaf)
              (node 3 leaf leaf))))

(sum-paths tt)