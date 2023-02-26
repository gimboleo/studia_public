#lang racket

(require rackunit)
(provide crack-caesar)

(define dict-empty null)

(define (dict-insert k v d)
  (if (null? d)
      (list (cons k v))
      (if (eq? k (caar d))
          (cons (cons k v) (cdr d))
          (cons (car d) (dict-insert k v (cdr d))))))

(define (dict-lookup k d)
  (if (null? d)
      'not-found
      (if (eq? k (caar d))
          (cdar d)
          (dict-lookup k (cdr d)))))

(define (to-assoc-list d) d)

(define (rotate-left n xs)
  (define m (modulo n (length xs)))
  (append (drop xs m) (take xs m)))

(define (zip xs ys)
  (if (null? xs)
      null
      (cons (cons (car xs) (car ys))
            (zip (cdr xs) (cdr ys)))))

(define (maximum xs)
  (define (aux x m) (if (> (cdr x) (cdr m)) x m))
  (if (null? xs) (error 'maximum "pamietaj, cholero, maximum nie dziala z lista dlugosci zero")
      (foldr aux (car xs) (cdr xs))))


(define (crack-caesar alphabet c xs)
  (define (find-index x acc alphabet)
    (if (eq? x (car alphabet))
        acc
        (find-index x (+ acc 1) (cdr alphabet))))

  (define (find-most-common xs dict)
    (if (null? xs) (maximum dict)
        (if (eq? (dict-lookup (car xs) dict) 'not-found)
            (find-most-common (cdr xs) (dict-insert (car xs) 1 dict))
            (find-most-common (cdr xs) (dict-insert (car xs) (+ (dict-lookup (car xs) dict) 1) dict)))))
  
  (define most-common (car (find-most-common xs dict-empty)))

  (define new-alphabet (rotate-left (- (find-index c 0 alphabet) (find-index most-common 0 alphabet)) alphabet))
  (define caesar-map (zip alphabet new-alphabet))

  (define (aux x m)
    (if (eq? x (caar m))
        (cdar m)
        (aux x (cdr m))))
  
  (map (lambda (x) (aux x caesar-map)) xs))



(define alphabet
  (let ([az (string->list "aąbcćdeęfghijklłmnńoópqrsśtuvwxyzźż")])
    (list* #\space #\. #\, #\! #\- #\: #\newline
           (append az (map char-upcase az)))))
(define (crack-string xs)
  (list->string (crack-caesar alphabet #\space (string->list xs))))
(define text
  "ŃukeĘsńwkeBvkĘGfeĘeqĄźłesńleśkteĘevźJtzfjKłGeĘGĘkumHGnexstmHowxleżsóńIeHsowsfjXketĆźĄośexsoewkeńzCnewsośBmkeńzeĘkutsjKxseńzCneńkĄxsfełGeBtĄGvkewzqsvGj-GmrfemzeżzuoqxlęeŁlńIezńĆlńeHkJkĄĆlfjZeĘzuzewzśkfekułzeĘHqkĄńGeĘkĄĆlg")

(check-equal? (crack-string text)
              "Dla widma sławy, w grób idą jak w łóżko,
Aby wywalczyć nikczemną piędź ziemi,
Na której nie ma dość miejsca do walki
Ani dość darni, by skryła mogiły
Tych, co polegną. Bądź odtąd zażartą,
O wolo moja, albo wzgardy wartą!")

(define text2 "RęcZtmóibZfpZflbccbZamkfaŻZ\nsrZręcZgmhcZfpZmlZk-lhflbŹ")
(check-equal? (crack-string text2) "The world is indeed comic, but the joke is on mankind.")