![Treść zadania](https://i.imgur.com/dDUCUM4.png)

[NRU](https://en.wikipedia.org/wiki/Page_replacement_algorithm#Not_recently_used)

Adresy: `0x000 0x004 0x010 0x084 0x03C 0x0E8 0xC8C 0x0A0 0x004 0x400 0x084 0x010 0x0E8 0x884 0xC8C 0x000`

| #   | Adres  | Tag | Index | Offset | Trafienie? | Replace |
| --- | ------ | --- | ----- | ------ | ---------- | ------- |
| 1   | 0x000  | 00  | 0     | 0      | comp. miss |         |
| 2   | 0x004  | 00  | 1     | 0      | comp. miss |         |
| 3   | 0x010  | 01  | 0     | 0      | comp. miss |         |
| 4   | 0x084  | 08  | 1     | 0      | comp. miss |         |
| 5   | 0x03c  | 03  | 3     | 0      | comp. miss |         |
| 6   | 0x0e8  | 0E  | 2     | 0      | comp. miss |         |
| 7   | 0xc8c  | C8  | 3     | 0      | comp. miss |         |
| 8   | 0x0a0  | 0A  | 0     | 0      | conf. miss | 00      |
| 9   | 0x004  | 00  | 1     | 0      | hit        |         |
| 10  | 0x400  | 40  | 0     | 0      | conf. miss | 01      |
| 11  | 0x084  | 08  | 1     | 0      | hit        |         |
| 12  | 0x010  | 01  | 0     | 0      | conf. miss | 0A      |
| 13  | 0x0e8  | 0E  | 2     | 0      | hit        |         |
| 14  | 0x0844 | 88  | 1     | 0      | conf. miss | 00      |
| 15  | 0x0c8c | C8  | 3     | 0      | hit        |         |
| 16  | 0x000  | 00  | 0     | 0      | conf. miss | 40      |

| Idx | Tag | Valid | Victim |
| --- | --- | ----- | ------ |
| 0   | 01  | 1     | +      |
| 0   | 00  | 1     |        |
| 1   | 88  | 1     |        |
| 1   | 08  | 1     | +      |
| 2   | 0E  | 1     |        |
| 2   |     | 0     |        |
| 3   | 03  | 1     | +      |
| 3   | C8  | 1     |        |

Potrzebne są $2$ bity na ofiarę według polityki NRU.

$hit \ ratio = \frac{4}{16} = 0.25$