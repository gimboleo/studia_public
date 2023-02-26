#lang racket

x

(let ([ x 3])
  (+ x y ) )

(let ([ x 1]
      [ y (+ x 2) ])
  (+ x y ) )

(let ([ x 1])
  ( let ([ y (+ x 2) ])
     (* x y ) ) )

( lambda ( x y )
   (* x y z ) )

(let ([ x 1])
  ( lambda ( y z )
     (* x y z ) ) )