from math import log10

#This function works only for positive natural numbers
def multiplication_table(x1, x2, y1 ,y2):
    spacing = int(log10(x2 * y2))   #Calculating how many digits the biggest number to print has so we can space-out the rest accordingly
    spacing_y = int(log10(y2))      #As above but only with the biggest y

    #Printing the first line (xs)
    print(" " * (spacing_y + 2), end = "") #+2 compensates for the empty space whereas usually there's a number
                                           #and for the fact that spacing is actually smaller by one than actual length of a number
    for x in range(x1, x2 + 1): print(" " * (spacing - int(log10(x))), x, end = "")
    print()

    #Printing the rest of the lines (ys and results)
    for y in range(y1, y2 + 1):
        print(" " * (spacing_y - int(log10(y))), y, end = "")
        for x in range(x1, x2 + 1):
            aux = x * y
            print(" " * (spacing - int(log10(aux))), aux, end = "")
        print()


multiplication_table(3, 5, 2, 4)
print()
multiplication_table(10, 20, 5, 10)