alphabet = input()
s = input()
n = int(input())



def query(str):
    if len(s) > len(str) + 1: return False

    try:
        j = -1

        for i, ch in enumerate(s):
            j += 1

            if ch == '?':
                if str[j] not in alphabet: return False

            elif ch == '*':
                aux = len(str) - len(s) + 1
                for bad in str[i : i + aux]:
                    if bad in alphabet: return False
                j += aux - 1

            else:
                if ch != str[j]: return False
    except: return False
    return len(str) == j + 1



for i in range(n): print('YES' if query(input()) else 'NO')