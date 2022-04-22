from itertools import zip_longest
import re

def criptarithm_solver(riddle):
    def letter_dict(l):
        if l not in dic: 
            i = 1 if l in first_chars else 0
            while i not in available and i < 10: i += 1
            if i > 9: return None
            dic[l] = i
            letters_stack.append(l)
            available.remove(i)
        return dic[l]       

    def failure():
        if not letters_stack: return False
        i = dic[letters_stack[-1]] + 1
        available.add(dic[letters_stack[-1]])
        while i not in available and i < 10: i += 1
        if i < 9: 
            dic[letters_stack[-1]] = i
            available.remove(i)
            return True
        else:
            dic.pop(letters_stack[-1])
            letters_stack.pop()
            return failure()

    words = re.split(' \+ | = ', riddle)

    rows = list(zip_longest(*map(reversed, words)))
    first_chars = set(w[0] for w in words)
    dic = {}
    letters_stack = []
    available = set(list(range(10)))

    r = 0
    rest = 0
    flag = False

    while r < len(rows):
        s = rest
        rest = 0
        for letter in rows[r][:-1]: 
            if letter != None: s += letter_dict(letter)

        rest = (s - s % 10) // 10
        if rows[r][-1] not in dic: 
            if s % 10 in available:
                dic[rows[r][-1]] = s % 10
                available.remove(s % 10)
                letters_stack.append(rows[r][-1])
            else: flag = True
        if flag or dic[rows[r][-1]] != s % 10:
            flag = False
            if failure(): 
                r = -1
                rest = 0
            else: return None
        r += 1
    
    return dic

print(criptarithm_solver("SEND + MORE = MONEY"))