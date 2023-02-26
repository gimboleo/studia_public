def fibonacci3(n):
    t1 = t2 = t3 = 1
    for i in range(3,n):
        t1,t2,t3 = t2,t3,t1+t2+t3
    print(t3)

fibonacci3(7)