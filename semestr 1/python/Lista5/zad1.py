def F(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1
        
def energia(a,i = 0):
    #print(a)
    if a == 1: return i
    return energia(F(a),i+1)
    
def statystyka(T):
    from statistics import median
    print("Średnia:",sum(T)/len(T))
    print("Mediana:",median(T))
    print("Max:",max(T))
    print("Min:",min(T))
    
    
def analiza_collatza(a,b):
    T = []
    for i in range(a,b+1):
        e = energia(i)
        print(i,": ",e,sep="")
        T.append(e)
    print("\nStatystyka:")    
    statystyka(T)

analiza_collatza(7,10)