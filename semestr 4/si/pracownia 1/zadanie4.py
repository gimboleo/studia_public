'''
Do rozwiązania zadania korzystam z arytmetyki binarnej i związanej z nią operatorów, żeby obliczyć liczbę zmian bitów potrzebnych
do uzyskania każdego z możliwych 'dobrych' rozwiązań.
Operacja XOR naszej liczby z takim rozwiązaniem da nam liczby z zapalonymi bitami tymi, które potrzebują zmiany.
Wystarczy wtedy tylko zliczyć liczbę zapalonych bitów aby uzyskać odpowiedż.
Kolejne 'dobre' rozwiązania można generować zwykłym przesunięciem bitowym w prawo.
'''


def bit_to_int(bits):
    res = 0
    for bit in bits: res = res * 2 + bit
    #for bit in bits: res = (res << 1) | bit
    return res


def opt_dist(bits, D):
    D = int(D)
    res = len(bits)
    number = int(bits, 2)
    mask = int('1' * D + '0' * (len(bits) - D), 2)

    for _ in range(len(bits) - D + 1): 
        res = min(res, bin(number ^ mask).count('1'))
        mask >>= 1

    return res


def opt_dist_int(bits, D):
    D = int(D)
    res = len(bits)
    number = bit_to_int(bits)
    mask = int('1' * D + '0' * (len(bits) - D), 2)

    for _ in range(len(bits) - D + 1): 
        res = min(res, bin(number ^ mask).count('1'))
        mask >>= 1

    return res



if __name__ == '__main__':
    with open('zad4_input.txt', mode='r') as in_file, open('zad4_output.txt', mode='w') as out_file:
        for line in in_file: 
            bits, D = line.split()
            out_file.write(f'{opt_dist(bits, D)}\n')