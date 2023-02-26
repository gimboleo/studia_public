#lang plait

(define (abs [x : Number])
  (if (< x 0)
      (- 0 x)
      x))

(define (average x y)
  (/ (+ x y) 2))

(define (sqrt [x : Number])
  (local
  [(define (improve [guess : Number][x : Number])
    (average guess (/ x guess)))

  (define (good-enough? [guess : Number][x : Number])
    (< (abs (- (* guess guess) x)) 0.001))

  (define (sqrt-iter [guess : Number][x : Number])
    (if (good-enough? guess x)
        guess
        (sqrt-iter (improve guess x)
                   x)))]
  (sqrt-iter 1.0 x)))

(define (square [x : Number])
  (* x x))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(define-type Vector
  (vector2 [x : Number] [y : Number])
  (vector3 [x : Number] [y : Number] [z : Number]))

(define (vector-length1 v)
  (if (vector2? v)
      (sqrt (+ (square (vector2-x v))
               (square (vector2-y v))))
      (sqrt (+ (square (vector3-x v))
               (+ (square (vector3-y v))
                  (square (vector3-z v)))))))

(define vec1
  (vector2 3 4))

(define vec2
  (vector3 1 1 1))

(display "vector-length1 wyrazenie warunkowe:\n")
(vector-length1 vec1)
(vector-length1 vec2)

(define (vector-length2 [v : Vector]) ;[v : Vector] --> typ argumentu
  (type-case Vector v                 ;sprawdza typ v
    [(vector2 x y)
     (sqrt (+ (* (vector2-x v)(vector2-x v))
              (* (vector2-y v)(vector2-y v))))]
    [else
     (sqrt (+ (* (vector3-x v)(vector3-x v))
              (+ (* (vector3-y v)(vector3-y v))
                 (* (vector3-z v)(vector3-z v)))))]))

(display "vector-length2 analiza przypadkow:\n")
(vector-length2 vec1)
(vector-length2 vec2)