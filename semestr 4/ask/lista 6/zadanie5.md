> **Zadanie 5.** Skompiluj poniższy kod źródłowy kompilatorem `gcc` z opcjami `«-Og -fomit-frame-pointer-fno-stack-protector»` i wykonaj deasemblację **jednostki translacji** przy użyciu programu `«objdump»`. Wytłumacz co robi procedura [alloca(3)](https://man7.org/linux/man-pages/man3/alloca.3.html), a następnie wskaż w kodzie maszynowym instrukcje realizujące przydział i zwalnianie pamięci. Wyjaśnij co robi robi instrukcja `«leave»`.
> ```c
> #include <alloca.h>
>
> long aframe(long n, long idx, long *q) {
>     long i;
>     long **p = alloca(n * sizeof(long *));
>     p[n-1] = &i;
>     for (i = 0; i < n; i++)
>         p[i] = q;
>     return *p[idx];
> }
> ```

# [gcc optimize options](https://gcc.gnu.org/onlinedocs/gcc/Optimize-Options.html)
# [flaga -fno-stack-protector](https://stackoverflow.com/questions/10712972/what-is-the-use-of-fno-stack-protector)
# [objdump](https://sourceware.org/binutils/docs/binutils/objdump.html)
# [Translation unit](https://en.wikipedia.org/wiki/Translation_unit_(programming))
# [Instrukcja leave](https://www.felixcloutier.com/x86/leave)

Instrukcja `«leave»` przechodzi do poprzedniej ramki stosu i jest równoważna poniższemu ciągowi instrukcji:
```assembly
mov %rbp, %rsp
pop %rbp
```

Deasemblacja dokonana za pomocą poniższych poleceń:
```bash
gcc -c -Og -fomit-frame-pointer -fno-stack-protector zadanie5.c
objdump zadanie5.o -d > zadanie5.txt
```