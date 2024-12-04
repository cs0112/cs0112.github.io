#lang racket

(define value 100)

(define (set-value! x)
  (set! value x))

(set-value! 5)
(printf "value: ~a~n" value)
