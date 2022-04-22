from src_redone import *
import unittest


class Test(unittest.TestCase):
    def test_valid(self):
        tests = [
            ('CIACHO + CIACHO == NADWAGA',
             {'N': 1, 'D': 5, 'I': 2, 'W': 7, 'C': 9,
              'G': 6, 'H': 3, 'A': 8, 'O': 4}),

            (('SO + MANY + MORE + MEN + SEEM + TO + '
              'SAY + THAT + THEY + MAY + SOON + TRY + '
              'TO + STAY + AT + HOME + SO + AS + TO + '
              'SEE + OR + HEAR + THE + SAME + ONE + MAN + '
              'TRY + TO + MEET + THE + TEAM + ON + THE + '
              'MOON + AS + HE + HAS + AT + THE + OTHER + '
              'TEN == TESTS'),
             {'H': 5, 'A': 7, 'R': 8, 'S': 3, 'T': 9,
              'M': 2, 'N': 6, 'E': 0, 'Y': 4, 'O': 1}),

            ('NUMBER + NUMBER == PUZZLE',
             {'P': 4, 'N': 2, 'U': 0, 'M': 1, 'Z': 3,
              'B': 6, 'L': 7, 'E': 8, 'R': 9}),

            ('A + BC == BC',
             {'B': 2, 'C': 1, 'A': 0}),

            ('TRZY + TRZY == SZEŚĆ',
             {'S': 1, 'T': 7, 'E': 3, 'R': 6, 'Ś': 0, 'Z': 5, 'Ć': 4, 'Y': 2}),

            ('1234567890 + 9876543210 == 11111111100',
             {'5': 5, '4': 6, '6': 4, '3': 7, '7': 3,
              '2': 8, '8': 2, '1': 1, '9': 9, '0': 0}),

            (('1234567890987654321 + 9876543210123456789 == '
              '11111111101111111110'),
             {'5': 5, '6': 6, '4': 4, '7': 7, '3': 3,
              '8': 8, '2': 2, '0': 0, '9': 9, '1': 1})
        ]

        for test in tests:
            self.assertEqual(cryptarithm_solver(test[0]), test[1])

    def test_invalid(self):
        tests = ['AB + CD == E', 'this + is + not + a == criptarithm']
        for test in tests:
            self.assertEqual(cryptarithm_solver(test), False)

    def test_formatting(self):
        tests = [
            ('SEND+MORE==MONEY',
             {'M': 1, 'S': 9, 'O': 0, 'R': 8, 'N': 6, 'Y': 2, 'E': 5, 'D': 7}),

            ('KIOTO     + OSAKA   == TOKIO',
             {'S': 2, 'I': 1, 'K': 4, 'T': 7, 'A': 0, 'O': 3}),

            ('THREE +THREE +TWO +TWO +ONE== ELEVEN',
             {'L': 7, 'H': 4, 'V': 2, 'T': 8, 'R': 6,
              'W': 0, 'N': 9, 'O': 3, 'E': 1}),

            ('A + ab == ab',
             {'a': 2, 'b': 1, 'A': 0})
        ]

        for test in tests:
            self.assertEqual(cryptarithm_solver(test[0]), test[1])


if __name__ == "__main__":
    unittest.main()
