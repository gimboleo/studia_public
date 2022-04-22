from itertools import permutations
import re
import time



def criptarithm_solver(riddle):
    words = re.split(' \+ | = ', riddle)
    characters = set(ch for w in words for ch in w)

    if len(characters) > 10: return None

    first_chars = set(w[0] for w in words)
    first_amount = len(first_chars)
    char_str = ''.join(first_chars) + ''.join(characters - first_chars)

    riddle_eq = riddle.replace('=', '==')

    for p in permutations('0123456789', len(characters)):

        if '0' in p[:first_amount]: continue
        
        try:
            if eval(riddle_eq.translate(riddle_eq.maketrans(char_str, ''.join(p)))): return dict(zip(char_str, p))
        except: continue

    return None



start_time = time.time()
print(criptarithm_solver("SEND + MORE = MONEY"))
print("--- %s seconds ---" % (time.time() - start_time))