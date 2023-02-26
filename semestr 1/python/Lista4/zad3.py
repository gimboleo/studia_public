import click
def perm(n):
    import random
    T = list(range(n))
    print(T)
    for i in range(n-1,0,-1):
        j = random.randint(0,i)
        tmp = T[i]
        T[i] = T[j]
        T[j] = tmp
    return T

for i in range(5):
    print(perm(10))
    print()

if click.confirm('10^6?', default=False):
    print(perm(10**6))