t = int(input())

for i in range(t):
    s = input()
    print('DA' if min(s.count('0'), s.count('1')) % 2 else 'NET')