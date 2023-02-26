import itertools
import time

def get_value(word, substitution):
    s = 0
    factor = 1
    for letter in reversed(word):
        s += factor * substitution[letter]
        factor *= 10
    return s

def solve2(equation):
    # split equation in left and right
    left, right = equation.lower().replace(' ', '').split('=')
    # split words in left part
    left = left.split('+')
    # create list of used letters
    letters = set(right)
    for word in left:
        for letter in word:
            letters.add(letter)
    letters = list(letters)

    digits = range(10)
    for perm in itertools.permutations(digits, len(letters)):
        sol = dict(zip(letters, perm))

        if len(str(get_value(right, sol))) != len(right): continue

        if sum(map(len,left)) != len(''.join(left)): continue

        if sum(get_value(word, sol) for word in left) == get_value(right, sol):
            print(' + '.join(str(get_value(word, sol)) for word in left) + ' =',get_value(right, sol))
            print(sol)
            break

start_time = time.time()
solve2('CIACHO + CIACHO = NADWAGA')
print("--- %s seconds ---" % (time.time() - start_time))
