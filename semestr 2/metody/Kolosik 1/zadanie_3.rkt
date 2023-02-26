#lang racket

Udowodnimy, że dla każdej procedury f i listy xs zachodzi (map-sum f xs) ≡ (sum (map f xs)).
(zakładamy, że wartościami procedury f są liczby)

Dowód przeprowadzimy indukcją strukturalną dla list.
Weźmy dowolną procedurę f, taką że jej wartościami są liczby.

Podstawa indukcji: (map-sum f null) ≡ (sum (map f null))
L ≡ (map-sum f null) ≡ (iter null 0) ≡ 0
P ≡ (sum (map f null)) ≡ (sum null) ≡ 0
Zatem L ≡ P

Krok indukcyjny:
Załóżmy, że zachodzi (map-sum f xs) ≡ (sum (map f xs))
Pokażemy, że to oznacza (map-sum f (cons x xs)) ≡ (sum (map f (cons x xs)))

L ≡ (map-sum f (cons x xs)) ≡
(iter (cons x xs) 0) ≡
(iter xs (+ (f x) 0)) ≡ (z arytmetyki)
(iter xs (f x)) ≡ (z lematu)
(+ (f x) (sum (map f xs)))

P ≡
(sum (map f (cons x xs))) ≡
(sum (cons (f x) (map f x))) ≡
(+ (f x) (sum (map f x)))

Zatem L ≡ P



Lemat:
(iter xs acc) ≡ (+ acc (sum (map f xs))) dla dowolnej wartości acc i procedury f (której wartościami są liczby)

Dowód przeprowadzimy indukcją strukturalną dla list.
Weźmy dowolną procedurę f, taką że jej wartościami są liczby.
Weźmy dowolną wartość acc.

Podstawa indukcji: (iter null acc) ≡ (+ acc (sum (map f null)))
L ≡ (iter null acc) ≡ acc
P ≡ (+ acc (sum (map f null))) ≡ (+ acc (sum null)) ≡ (+ acc 0) ≡ (z arytmetyki) acc
Zatem L ≡ P

Krok indukcyjny:
Załóżmy, że zachodzi (iter xs acc) ≡ (+ acc (sum (map f xs)))
Pokażemy, że to oznacza (iter (cons x xs) acc) ≡ (+ acc (sum (map f (cons x xs))))
L ≡ (iter (cons x xs) acc) ≡
(iter xs (+ (f x) acc)) ≡ (z założenia)
(+ (+ (f x) (acc)) (sum (map f xs))) ≡ (z arytmetyki)
(+ (f x) (acc) (sum (map f xs))) ≡ (z def. sum)
(+ acc (sum (cons (f x) (map f xs)))) ≡ (z def. map)
(+ acc (sum (map f (cons x xs)))) ≡ R