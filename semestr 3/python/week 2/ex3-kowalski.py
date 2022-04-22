import time

#This function works properly only for whole numbers
def F(n, x, y):
    if n < 0: return 0
    if n == 0: return x + y
    if y == 0: return x
    return F(n - 1, F(n, x, y - 1), F(n, x, y - 1) + y)

def memoize(f):                                             #Function that memoizes given function using a dictionary
    cache = {}
    def aux(*x):
        if x not in cache:
            cache[x] = f(*x)
        return cache[x]
    return aux

@memoize
def Fm(n, x, y):
    if n < 0: return 0
    if n == 0: return x + y
    if y == 0: return x
    return Fm(n - 1, Fm(n, x, y - 1), Fm(n, x, y - 1) + y)



#All correct answers were taken from Wikipedia
print("F(0,2,6): ")

start = time.time()
print(F(0, 4, 6))                                       
print("--- %s seconds ---" % (time.time() - start))

start = time.time()
print(Fm(0, 4, 6))                                          #10
print("--- %s seconds ---" % (time.time() - start))

print()


#The F function starts to run non-instantly from about here for n = 1
print("F(1,13,20): ")

start = time.time()
print(F(1, 13, 20))                                       
print("--- %s seconds ---" % (time.time() - start))

start = time.time()
print(Fm(1, 13, 20))                                        #245744
print("--- %s seconds ---" % (time.time() - start))

print()


print("F(19,5,0): ")

start = time.time()
print(F(19, 5, 0))                                         
print("--- %s seconds ---" % (time.time() - start))

start = time.time()
print(Fm(19, 5, 0))                                         #5
print("--- %s seconds ---" % (time.time() - start))

print()


#For n = 2 the original function can calculate only the most basic of cases (x = 0 or y < 2, F(2, 1, 2) seems to be the limit)
print("F(2,1,2): ")

start = time.time()
print(F(2, 1, 2))                                         
print("--- %s seconds ---" % (time.time() - start))

start = time.time()
print(Fm(2, 1, 2))                                          #10228
print("--- %s seconds ---" % (time.time() - start))

print()


print("F(2,5,2): ")

#start = time.time()
#print(F(2, 5, 2))                                          #Commented this one out, 5 minutes wasn't enough for my pc to calculate it
#print("--- %s seconds ---" % (time.time() - start))

start = time.time()
print(Fm(2, 5, 2))                                          #~5.02*10^135
print("--- %s seconds ---" % (time.time() - start))

#Calculating for bigger x's and n's breaks