#lang racket

(define first-contract
  (parametric->/c [a b] (-> (-> a b) a b)))

(define second-contract
  (parametric->/c [a b c] (-> (-> a b c)
                              (-> (cons/c a b) c))))

(define third-contract 
  (parametric->/c [a b] (-> (listof (-> a b))
                            (listof a)
                            (listof b))))

(define fourth-contract
  (parametric->/c [a b] (-> (-> b (or/c false/c (cons/c a b)))
                            b
                            (listof a))))

(define fifth-contract
  (parametric->/c [a] (-> (-> a boolean?)
                          (listof a)
                          (cons/c (listof a) (listof a)))))

;; Napisz poniżej implementacje procedur spełniające powyższe kontrakty

(define/contract (first f x)
  first-contract
  (f x))

(first (lambda (x) (+ x 1)) 5)



(define/contract (second f)
  second-contract
  (lambda (x) (f (car x) (cdr x))))

((second +) (cons 3 2))



(define/contract (third fs xs)
  third-contract
  (if (or (null? fs) (null? xs))
      null
      (cons ((car fs) (car xs)) (third (cdr fs) (cdr xs)))))

(third (list identity not string?) (list 5 #t "test"))



(define/contract (fourth f x)
  fourth-contract
  (let [(res (f x))]
    (if (equal? res #f)
        null
        (list (car res)))))

(fourth (lambda (x) (if (string? x) (cons "string" x) #f)) "abc")



(define/contract (fifth pred xs)
  fifth-contract
  (define (aux xs res)
    (if (null? xs)
        res
        (if (pred (car xs))
                  (aux (cdr xs) (cons (cons (car xs) (car res)) (cdr res)))
                  (aux (cdr xs) (cons (car res) (cons (car xs) (cdr res)))))))
  (aux xs (cons null null)))

(car (fifth even? (list 1 2 3 4 5 6)))
(cdr (fifth even? (list 1 2 3 4 5 6)))