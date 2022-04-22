#This function works only for whole numbers, including negative ones
def multiplication_table(x1, x2, y1 ,y2):
    spacing = max(map(lambda i: len(str(i)), (x1, x2, y1, y2, x1 * y1, x1 * y2, x2 * y1, x2 * y2)))
    #Calculating how many digits the longest number to print has so we can space-out the rest accordingly
    spacing_y = max(len(str(y2)), len(str(y1)))                                #As above but only with ys

    #Printing the first line (xs)
    print(" " * (spacing_y + 1), end = "") #+1 compensates for the empty space whereas usually there's a number
    for x in range(x1, x2 + 1): print(" " * (spacing - len(str(x))), x, end = "")
    print()

    #Printing the rest of the lines (ys and results)
    for y in range(y1, y2 + 1):
        print(" " * (spacing_y - len(str(y))), y, end = "")
        for x in range(x1, x2 + 1):
            aux = x * y
            print(" " * (spacing - len(str(aux))), aux, end = "")
        print()


multiplication_table(3, 5, 2, 4)
print()
multiplication_table(10, 20, 0, 10)
print()
multiplication_table(-10, 10, -1, 7)
print()
multiplication_table(-5, 3, 0, 0)
print()
multiplication_table(5, 0, 0, 5)
print()
multiplication_table(10, -10, 10, -10)