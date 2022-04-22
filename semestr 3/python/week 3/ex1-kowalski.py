from timeit import timeit

reps = 10 ** 3
primes_100 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
primes_20 = [2, 3, 5, 7, 11, 13, 17, 19]



#As stated in the task, all functions work for natural numbers
#I chose not to implement the Sieve of Eratosthenes as I didn't know how to do it properly non-imperatively 

''' Getting rid of the square root speeds up the function significantly
def prime_imperative_square(n):
    if n < 2: return []
    res = [2]
    for i in range(3, n, 2): 
        if all (i % d for d in range(2, int(i ** 0.5) + 1)): res.append(i)
    return res
'''

def prime_imperative(n):
    if n <= 2: return []
    res = [2]                   #We start with 2 - the only even prime (bigger even numbers are divisible by 2)
    for i in range(3, n, 2):    #Thanks to this we can operate only on odd numbers, reducing the amount of iterations by half
        j = 2
        flag = False            #For each number we'll check if it's divisible by other numbers than one and itself
        while j * j <= i:       #We can stop checking after sqrt(i), because sqrt(i) is the biggest possible factor of i
            if not i % j:
                flag = True
                break
            j += 1
        if not flag: res.append(i)
    return res

def prime_comprehension(n): 
    #Again, checking only odd numbers greatly speeds up the function
    #Although I wasn't able to get rid of the square root without adding things outside the list comprehension
    #*(iterable) unpacks an iterable
    #all(iterable) returns True if all elements of an iterable are true or if an iterable is empty
    return [2, *(i for i in range(3, n, 2) if all(i % d for d in range(2, int(i ** 0.5) + 1)))] if n > 2 else []

def prime_functional(n): 
    return [2] + list(filter(lambda x: all(map(lambda y: x % y, range(2, int(x ** 0.5 + 1)))), range(3, n, 2))) if n > 2 else []

functions = [prime_imperative, prime_comprehension, prime_functional]



for f in functions: print(f(2))
print()

for f in functions: print(f(20))
print(primes_20)
print()

for f in functions: print(f(100))
print(primes_100)
print()



print([isinstance(l, list) for l in [f(100) for f in functions]])
print()



for i in range(1, 5):
    x = 10 ** i
    print(x, ':', sep = '')
    print('Imperative:', timeit(f'prime_imperative({x})', 'from __main__ import prime_imperative', number = reps))
    print('Comprehension:', timeit(f'prime_comprehension({x})', 'from __main__ import prime_comprehension', number = reps))
    print('Functional:', timeit(f'prime_functional({x})', 'from __main__ import prime_functional', number = reps))
    print()

print('100000:')
print('Imperative:', timeit('prime_imperative(100000)', 'from __main__ import prime_imperative', number = 10))
print('Comprehension:', timeit('prime_comprehension(100000)', 'from __main__ import prime_comprehension', number = 10))
print('Functional:', timeit('prime_functional(100000)', 'from __main__ import prime_functional', number = 10))

'''
Conclusions from testing:
- The imperative function performs the best with smaller n but eventually it loses its advantage
- prime_comprehension() and prime_functional() perform similarly, but prime_comprehension() seems a bit faster overall
'''