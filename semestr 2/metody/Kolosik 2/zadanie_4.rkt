#lang plait

;; Typ drzew prefiksowych

(define-type (PrefixTree 'a)
    (node [exists : Boolean] [children : (Listof ('a * (PrefixTree 'a)))]))

;; Przykładowe drzewo prefiksowe z treści zadania

(define example-tree
  (node #f (list
    (pair 1 (node #t (list
      (pair 2 (node #f (list
        (pair 3 (node #t empty))
        (pair 4 (node #t empty))))))))
    (pair 3 (node #f (list
      (pair 5 (node #t empty))))))))

;; Napisz implementacje procedur poniżej

(lookup : ((Listof 'a) (PrefixTree 'a) -> Boolean))
(define (lookup xs t)
  (if (empty? xs)
      (node-exists t)
      (foldr (lambda (a b) (or (and (equal? (fst a) (first xs)) (lookup (rest xs) (snd a))) b)) #f (node-children t))))

(lookup (list 1 2 4) example-tree)
         
  

(insert : ((Listof 'a) (PrefixTree 'a) -> (PrefixTree 'a)))
(define (insert xs t)
  ;; XXX: uzupełnij
  (error 'insert "Not implemented!"))

(remove : ((Listof 'a) (PrefixTree 'a) -> (PrefixTree 'a)))
(define (remove xs t)
  ;; XXX: uzupełnij
  (error 'remove "Not implemented!"))