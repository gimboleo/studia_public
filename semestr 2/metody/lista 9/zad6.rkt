#lang racket

(define (lists-prog program)
  `(let (null 0)
     (let (null? (lambda (x) (and (number? x) (= x null))))
       ,program)))


(define (sort-i l)
  (define (insert e l)
    (if (null? l)
        (list e)
        (let ((x (car l))
              (xs (cdr l)))
          (if (< e x) 
              (cons e l)
              (cons x (insert e xs))))))
  (if (null? l) 
      l
      (insert (car l) (sort-i (cdr l)))))


(define (sort-prog xs)
  `(letrec (insert
            (lambda (e l)
              (if (null? l)
                  (pair e null)
                  (let (x (fst l))
                    (let (xs (snd l))
                      (if (< e x) 
                          (pair e l)
                          (pair x (insert e xs))))))))
     (letrec (sort
              (lambda (l)
                (if (null? l) 
                    l
                    (insert (fst l) (sort (snd l))))))
       (sort ,xs))))

(define (test-sort n)
  (define (randomlist n)
    (if (= n 0) null
        (cons (random 1000) (randomlist (- n 1)))))
  (define (list->prog l)
    (if (null? l) 'null `(pair ,(car l) ,(list->prog (cdr l)))))
  (let* ((l (randomlist n))
         (l1 (list->prog l))
         (prog (parse (lists-prog (sort-prog l1 )))))
    (begin (display "racket:")
           (displayln (sort-i l))
           (display "nasz: ")
           (eval prog))))