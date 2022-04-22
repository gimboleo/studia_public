def multiplication_table(x1: int, x2: int, y1: int, y2: int) -> str:
    """Creates a graphical representation of a multiplication table

    Arguments
    Works for whole numbers, including negative ones
    All ranges are inclusive
    ----------
    x1 : int
        Lower range for the columns
    x2 : int
        Upper range for the columns
    y1 : int
        Lower range for the rows
    y2 : int
        Upper range for the rows

    Returns a string containing the table in a human-readable format
    """

    spacing = max(map(lambda i: len(str(i)),
                      (x1, x2, y1, y2, x1 * y1, x1 * y2, x2 * y1, x2 * y2)))
    # Calculating how many digits the longest number to print has
    # so we can space-out the rest accordingly
    spacing_y = max(len(str(y2)), len(str(y1)))  # As above but only with ys

    # Handling the first line (xs)
    # +1 compensates for the empty space whereas usually there's a number
    res = " " * (spacing_y + 1)
    for x in range(x1, x2 + 1):
        res += f'{" " * (spacing - len(str(x)))} {x}'
    res += "\n"

    # Handling the rest of the lines (ys and results)
    for y in range(y1, y2 + 1):
        res += f'{" " * (spacing_y - len(str(y)))} {y}'
        for x in range(x1, x2 + 1):
            aux = x * y
            res += f'{" " * (spacing - len(str(aux)))} {aux}'
        res += "\n"

    return res


if __name__ == '__main__':
    print(multiplication_table(3, 5, 2, 4))
    print()
    print(multiplication_table(10, 20, 0, 10))
    print()
    print(multiplication_table(-10, 10, -1, 7))
    print()
    print(multiplication_table(-5, 3, 0, 0))
    print()
    print(multiplication_table(5, 0, 0, 5))
    print()
    print(multiplication_table(10, -10, 10, -10))
