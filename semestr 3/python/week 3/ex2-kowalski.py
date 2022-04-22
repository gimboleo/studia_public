from timeit import timeit
from itertools import chain

reps = 10 ** 3 * 2
perfect_50 = [6, 28]
perfect_10000 = [6, 28, 496, 8128]



#As stated in the task, all functions work for natural numbers

def perfect_imperative(n):
    res = []
    for i in range(2, n):                   #0 and 1 obviously aren't perfect and they break calculations, so we exclude them
        s, j = 1, 2                         #1 divides every natural number, therefore we initialize the sum with it
        while j * j < i:              
            if not i % j: s += j + i // j   #If i is divisible by j, then it's also divisible by i/j
            j += 1
        if j * j == i: s += j               #We examine sqrt(i) separately to avoid counting it twice using the method above
        if s == i: res.append(i)
    return res

def perfect_comprehension(n):
    #Here we use the set to avoid possible square root duplication
    #We don't include 1 in the set, so we compare its sum to i - 1 instead of i
    return [i for i in range(2, n) if sum({d for j in range(2, int(i ** 0.5) + 1) if not i % j for d in (j, i // j)}) == i - 1]

def perfect_functional(n):
    #itertools.chain.from_iterable(iterable) gets chained inputs from a single iterable and unchains them into a single iterator
    #Firstly, we put all divisors of x up to sqrt(x) in an iterator, then add the remaining ones (x // y) using map, then we pack everything into a set
    #We don't include 1 in the set, so we compare its sum to i - 1 instead of i
    return list(filter(lambda x: sum(set(chain.from_iterable(map(lambda y: (y, x // y), filter(lambda z: not x % z, range(2, int(x ** 0.5) + 1)))))) == x - 1, range(2, n)))

functions = [perfect_imperative, perfect_comprehension, perfect_functional]



for f in functions: print(f(2))
print()

for f in functions: print(f(50))
print(perfect_50)
print()

for f in functions: print(f(10000))
print(perfect_10000)
print()



print([isinstance(l, list) for l in [f(100) for f in functions]])
print()



for i in range(1, 4):
    x = 10 ** i
    print(x, ':', sep = '')
    print('Imperative:', timeit(f'perfect_imperative({x})', 'from __main__ import perfect_imperative', number = reps))
    print('Comprehension:', timeit(f'perfect_comprehension({x})', 'from __main__ import perfect_comprehension', number = reps))
    print('Functional:', timeit(f'perfect_functional({x})', 'from __main__ import perfect_functional', number = reps))
    print()

print('10000:')
print('Imperative:', timeit('perfect_imperative(10000)', 'from __main__ import perfect_imperative', number = 100))
print('Comprehension:', timeit('perfect_comprehension(10000)', 'from __main__ import perfect_comprehension', number = 100))
print('Functional:', timeit('perfect_functional(10000)', 'from __main__ import perfect_functional', number = 100))

'''
Conclusions from testing:
- The functional function performs the worst, especially with medium-sized n
- The imperative one seems to be better with smaller n, the comprehension one with bigger n
  (it is possible that the functional one performs better than the imperative one 
  for sufficiently big n but I didn't have the patience to test it)
'''