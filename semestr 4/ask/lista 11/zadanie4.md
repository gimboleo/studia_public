![Treść zadania](https://i.imgur.com/VgUy2n1.png)

Mamy $1$ zbiór, $8$ bloków po jednym wierszu każdy.

Adresy: `0 4 10 84 3c e8 c8c a0 4 400 84 10 e8 884 c8c 0`

| addr | TAG | OFF | conflict | compulsory | victim (slot) |
| ---- | --- | --- | -------- | ---------- | ------ |
| 0    | 0   |  0  |    N     |      T     |   -    |
| 4    | 1   |  0  |    N     |      T     |   -    |
| 10   | 4   |  0  |    N     |      T     |   -    |
| 84   | 21  |  0  |    N     |      T     |   -    |
| 3c   | f   |  0  |    N     |      T     |   -    |
| e8   | 3a  |  0  |    N     |      T     |   -    |
| c8c  | 323 |  0  |    N     |      T     |   -    |
| a0   | 28  |  0  |    N     |      T     |   -    |
| 4    | 1   |  0  |    N     |      N     |   -    |
| 400  | 100 |  0  |    T     |      N     |   0    |
| 84   | 21  |  0  |    N     |      N     |   -    |
| 10   | 4   |  0  |    N     |      N     |   -    |
| e8   | 3a  |  0  |    N     |      N     |   -    |
| 884  | 221 |  0  |    T     |      N     |   4    |
| c8c  | 323 |  0  |    N     |      N     |   -    |
| 0    | 0   |  0  |    T     |      N     |   7    |

| Tag | Valid | Last used        |
| --- | ----- | ---------------- |
|  100| 1     |        6         |
|  1  | 1     |        7         |
|  4  | 1     |        4         |
|  21 | 1     |        5         |
|  221| 1     |        2         |
|  3a | 1     |        3         |
|  323| 1     |        1         |
|  0  | 1     |        0         |

Potrzebne są $3$ bity na ofiarę według polityki LRU.

$hit \ ratio = \frac{5}{16} = 0.3125$