def pot(a, b):
    x = 0
    rez = 1
    while b>0:
        if b%2:
            rez = rez * a
            x = x + 1
        b = b // 2
        a = a * a
        x = x + 1
    return x

M = m = pot(6,1024)
liczbaM = liczbam = 1024
for i in range(1025,2048):
    if pot(6,i) > M:
        M = pot(6,i)
        liczbaM = i
    if pot(6,i) < m:
        m = pot(6,i)
        liczbam = i

print(liczbam,m)
print(liczbaM,M)
print(pot(6,512))
print(pot(6,1023))