from re import split as resplit
from itertools import zip_longest

# I did not implement the * and / operators
# I didn't know how to do it without resorting to brue force

# Subtraction seems feasible but I ran out of time :c


def cryptarithm_solver(riddle: str) -> dict[str, int] | bool:
    '''A recursive function solving criptarithms that uses backtracking

    Returns a valid solution (in the form of a dictionary)
    or False if there is none

    In a sense, it emulates manual addition
    to discard invalid partial solutions.

    Additional criteria of a valid cryptarithm solution not stated in the task
    (but listed on the link provided in the task sheet or on cryptarithms.com):
        -Each letter represents an unique digit
        -Numbers don't have leading zeros
        (0 itself is an exception and is allowed)

    Input should look like a valid python expression
    built with + and == operators and digits
    (but with characters instead of digits)

    Additionally, only one number (word) to the right of == is allowed
    '''

    # A single instance of this function
    # is working on a single letter in the equation
    def aux(col, row, dic, s):
        if col >= len(rows):      # If we checked all rows and there's no carry
            return not s and dic  # we found our solution
        letter = rows[col][row]
        if row < len(rows[col]) - 1:  # Letters to the left of == operator
            if not letter:  # There's no letter at that index -> we carry on
                return aux(col, row + 1, dic, s)
            # The letter is already asigned, we carry on with an increased sum
            if letter in dic:
                return aux(col, row + 1, dic, s + dic[letter])
            else:
                # We asign the next unasigned digit to the given letter
                # and try to carry on recursively
                # If successful, we return the solution
                # If not, we try with the next available digit
                # If we ran out of digits, we return False
                for i in range(1 if letter in first_chars else 0, 10):
                    if i not in dic.values():
                        res = aux(col, row + 1, {letter: i, **dic}, s + i)
                        if res:
                            return res
                return False
        else:  # Letters to the right of == operator
            r = s // 10  # Carry to be transferred to the next column
            s = s % 10  # Actual sum from 0 to 9 that we can assign to a letter
            # Addition won't create results shorter than the addends
            if not letter:
                return False
            # If letter is already asigned,
            # we check if it matches the calculated sum

            # If it does, we carry on recursively to the next column;
            # If not, we return False
            if letter in dic:
                return aux(col + 1, 0, dic, r) if dic[letter] == s else False
            else:
                if s in dic.values():
                    # If the calculated sum is already asigned, we return False
                    return False
                # If the sum = 0 and asigning it
                # would create a trailing zero, we return false
                if letter in first_chars and s == 0:
                    return False
                # If the conditions above were not met,
                # we can safely carry on to the next column
                return aux(col + 1, 0, {letter: s, **dic}, r)

    # A list of all words
    words = resplit('\+|==', ''.join(riddle.split()))
    # A set with letters that can't be set to 0
    first_chars = set(w[0] for w in words if len(w) > 1)
    # We want to emulate the alignment of letters
    # that would be created if we were to perform a manual addition
    # (as shown in the example cryptarithm on the task sheet)

    # We group letters into a list of tuples,
    # each tuple represents a single column of letters

    # Each index in the tuple represents a single row
    # If there's no letter at the given indexes, it's place is filled with None
    rows = list(zip_longest(*map(reversed, words)))

    return aux(0, 0, {}, 0)


if __name__ == '__main__':
    from time import time

    # A simple function used for printing out the solutions and testing
    def solution_checker(s):
        print(s)
        start = time()
        res = cryptarithm_solver(s)
        stop = time() - start
        print(res)

        if res:
            dic = {ord(k): str(v) for k, v in res.items()}
            solution = s.translate(s.maketrans(dic))
            print(solution, eval(solution))

        print("--- %s seconds ---" % stop)

    phrases = [
        "CIACHO + CIACHO == NADWAGA",
        "SEND+MORE==MONEY",
        "KIOTO     + OSAKA   == TOKIO",
        "THREE +THREE +TWO +TWO +ONE== ELEVEN",
        ("SO + MANY + MORE + MEN + SEEM + TO + SAY + "
         "THAT + THEY + MAY + SOON + TRY + TO + STAY + "
         "AT + HOME + SO + AS + TO + SEE + OR + HEAR + "
         "THE + SAME + ONE + MAN + TRY + TO + MEET + THE + "
         "TEAM + ON + THE + MOON + AS + HE + HAS + AT + "
         "THE + OTHER + TEN == TESTS"),
        # I didn't find a longer valid cryptarithm in the internet
        # and it calculates in less than 2 seconds
        "this + is + not + a == criptarithm",
        "A + BC == BC",
        "AB + CD == E",
        "NUMBER + NUMBER == PUZZLE",
        # This function treats characters as equal only if python does so
        "A + ab == ab",
        "TRZY + TRZY == SZE????",
        "1234567890 + 9876543210 == 11111111100",
        "1234567890987654321 + 9876543210123456789 == 11111111101111111110"
    ]

    for p in phrases:
        cryptarithm_solver(p)
        # solution_checker(p)
        # print("\n\n")
