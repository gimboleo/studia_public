def kwadrat1(n):
    for i in range(n):
        for j in range(n):
            print("*", end=" ")
        print()

def kwadrat2(n):
    for i in range(n):
        for j in range(n):
            print("#", end="")
        print()

for i in range(10):
    print("Przebieg: ", i)
    print(20 * "-")
    if i<=4:
        kwadrat1(2*i+3)
    else:
        kwadrat2(i-5+3)
    print()