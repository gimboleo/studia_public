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


(define (fold-tree f i t)
  (if (leaf? t)
      i
      (f (node-val t)
         (fold-tree f i (node-left t))
         (fold-tree f i (node-right t)))))


(define (tree-sum t) (fold-tree + 0 t))

(define (flip t)
  (fold-tree
   (lambda (a b c) (node a c b))
   leaf
   t))

(define (height t)
  (fold-tree
   (lambda (a b c) (+ 1 (max b c)))
   0
   t))

(define (tree-span t)
  (fold-tree
   (lambda (a b c)
     (cond
       [(eq? (car b) leaf)
        (if (eq? (cdr c) leaf)
            (cons a a)
            (cons a (cdr c)))]
       [(eq? (cdr c) leaf)
        (if (eq? (car b) leaf)
            (cons a a)
            (cons (car b) a))]
       [else (cons (car b) (cdr c))]))
   (cons leaf leaf)
   t))

(define (tree-max t) (fold-tree max -inf.0 t))


(define t
  (node 5 (node 2 leaf leaf)
        (node 8 (node 6 leaf leaf)
              (node 9 leaf leaf))))

(tree-sum t)
(flip t)
(height t)
(tree-span t)
(tree-max t)