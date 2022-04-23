> **Zadanie 5.** Uzupełnij ciało funkcji zadeklarowanej następująco:
> ```c
> /* Oblicz x * 3 / 4 zaokrąglając w dół. */
> int32_t threefourths(int32_t x);
> ```
>> **Uwaga!** Nie można dopuścić do wystąpienia nadmiaru i niedomiaru!

```c
/* Oblicz x * 3 / 4 zaokrąglając w dół. */
int32_t threefourths(int32_t x) {
    return (x >> 1) + (x + 1 >> 2)
}
```

`(x >> 1)` $\equiv \lfloor\frac{x}{2}\rfloor$  
`(x + 1 >> 2)` $\equiv \lfloor\frac{x + 1}{4}\rfloor$

- $x \equiv 0 \space mod \space 4$  
$\lfloor\frac{3x}{4}\rfloor = \frac{3x}{4} = \frac{x}{2} + \frac{x}{4} = \lfloor\frac{x}{2}\rfloor + \lfloor\frac{x + 1}{4}\rfloor$

- $x \equiv 1 \space mod \space 4$  
$\lfloor\frac{3x}{4}\rfloor = \frac{3x - 3}{4} = \frac{x - 1}{2} + \frac{x - 1}{4} = \lfloor\frac{x}{2}\rfloor + \lfloor\frac{x + 1}{4}\rfloor$

- $x \equiv 2 \space mod \space 4$  
$\lfloor\frac{3x}{4}\rfloor = \frac{3x - 2}{4} = \frac{x}{2} + \frac{x - 2}{4} = \lfloor\frac{x}{2}\rfloor + \lfloor\frac{x + 1}{4}\rfloor$

- $x \equiv 3 \space mod \space 4$  
$\lfloor\frac{3x}{4}\rfloor = \frac{3x - 1}{4} = (\frac{x - 1}{2} + \frac{1}{2}) + (\frac{x + 1}{4} - \frac{1}{4}) - \frac{1}{4} = \lfloor\frac{x}{2}\rfloor + \lfloor\frac{x + 1}{4}\rfloor$
