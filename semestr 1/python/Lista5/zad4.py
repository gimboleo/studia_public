#l3=list(zip(list1,list2))

def usun_duplikaty(T1):
    T2 = list(range(0,len(T1)))
    T3=list(zip(T1,T2))
    print(T3)
    T3.sort()
    print(T3)
    T4 = []
    x = T3[0][0]
    T4.append(T3[0])
    for i in range(1,len(T3)):
        if T3[i][0] != x:
            x = T3[i][0]
            T4.append(T3[i])
    print(T4)
    T4.sort(key=lambda x:x[1])
    print(T4)
    T5 = [i[0] for i in T4]
    print(T5)


T = [2,6,2,8,3,2,5,7,8,2,8,6,9,7]
usun_duplikaty(T)
