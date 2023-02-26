#lang plait

(define-type (RoseTree 'a)
    (leaf)
    (rosenode [val : 'a] [li : (Listof (RoseTree 'a))]))
    
    
(define (preorder t)
    (cond
        [(leaf? t) empty]
        [(rosenode? t) (cons (rosenode-val t)
                             (foldr (lambda (x y)
                             ; append jest nieladny
                             (append (preorder x) y))
                              empty
                              (rosenode-li t)))]))
                              
(define (preorder1 t)
    (local [(define (pom t acc)
        (type-case (RoseTree 'a) t
            [(leaf) acc]
            [(rosenode val li) (cons val
;( foldr :((RoseTree 'a)  (Listof 'a) -> (Listof 'a)) 
;         (Listof 'a) 
;         (Listof (RoseTree 'a)) -> (Listof 'a))
                                     (foldr pom acc li))]))]
(pom t empty)))