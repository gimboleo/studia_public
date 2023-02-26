![Treść zadania](https://i.imgur.com/FOz4ax0.png)

- Blok ma $4$ bajty $\rightarrow 2$ bity na offset 
- Indeksy $0-3 \rightarrow 2$ bity na indeks 
- $12 - 4 = 8$ bitów na tag

---

- `0x832` $\rightarrow$ `0x83 00 10` $\rightarrow$ HIT $\rightarrow$ `0xCC`
- `0x835` $\rightarrow$ `0x83 01 01` $\rightarrow$ MISS (INVALID)
- `0xFFD` $\rightarrow$ `0xFF 11 01` $\rightarrow$ HIT $\rightarrow$ `0xC0`

---

- `0x4A` $\rightarrow$ `0x00 10 10` $\rightarrow$ `0x00A`