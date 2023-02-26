#lang plait

(define (prefixes xs)
  (if (empty? xs)
      (list empty)
      (cons empty (map (lambda (ys) (cons (first xs) ys)) (prefixes (rest xs))))))

(prefixes (list 1 2 3 4 5))