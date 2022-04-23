'''
Pierwsza część rozwiązania sprowadza się do znalezienia wszystkich możliwych początków słów dla wszystkich możliwych końców słów.
Wychodząc od początku linijki (lub wcześniej znalezionych końców słów) znajdujemy kolejne końce słów.

Posiadając już powyższe informacje będziemy (zaczynając od końca) liczyć wszystkie możliwe sumy kwadratów długości słów i
propagować 'największe' rozwiązanie (w postaci sum kwadratów i miejsc, w które trzeba wstawić spacje) na początek.

Na sam koniec wstawiamy spacje w odpowiednie miejsca i zwracamy nowy napis.

(Według zasady z polecenia każde słowo powinno należeć do zbioru s - 
założyłem więc, że każdy napis da się rozbić na wyrazy z słownika.
Jeśli program natrafiłby na takie wyrażenie, zostawiłby linijkę niezmienioną.)
'''


def add_spaces(S, t):
    word_end = [0 for _ in range(len(t))]
    starts_for_ends = [[] for _ in range(len(t))]

    for i in range(len(t)):
        if word_end[i - 1]:
            for j in range(i, len(t)):
                if t[i:j+1] in S:
                    word_end[j] = 1
                    starts_for_ends[j].append(i)
        if t[:i+1] in S: 
            word_end[i] = 1
            starts_for_ends[i].append(0)

    max_word = [[0, []] for _ in range(len(t) + 1)]
    valid = [False for _ in range(len(t))]
    valid[-1] = True

    for end in range(len(t) - 1, -1, -1):
        if valid[end]:
            for start in starts_for_ends[end]:
                val = max_word[end + 1][0] + (end - start + 1) ** 2
                if val > max_word[start][0]:
                    max_word[start] = [val, [start - 1] + max_word[end + 1][1]]
                    valid[start - 1] = True

    if max_word[0][1][1:]:
        x = max_word[0][1][1]
        res = t[0:x+1]
        for space in max_word[0][1][2:]:
            res += ' ' + t[x+1:space+1]
            x = space
        res += ' ' + t[x+1:]
    else: res = t

    #print(res)
    return res



if __name__ == '__main__':
    with open('pan_tadeusz_bez_spacji.txt', mode='r') as in_file, open('words_for_ai1.txt') as dict_file, open('zad2_output.txt', mode='w') as out_file:
    #with open('zad2_input.txt', mode='r') as in_file, open('words_for_ai1.txt') as dict_file, open('zad2_output.txt', mode='w') as out_file:
        dict = set(dict_file.read().splitlines())
        for line in in_file: out_file.write(f'{add_spaces(dict, line.strip())}\n')