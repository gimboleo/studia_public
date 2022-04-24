> **Zadanie 9 (bonus).** Przetłumacz kod poniższej funkcji o sygnaturze `«float puzzle9(float, float)»` na język C, po czym jednym zdaniem powiedz co ona robi.
>> **Wskazówka:** Znaczenie pierwszego operandu instrukcji `«vroundsd»` jest wyjaśnione w tabeli $4-18$ zawartej w dokumencie „Intel® 64 and IA-32 Architectures Software Developer’s Manual Volume 2: Instruction Set Reference, A-Z” pod opisem instrukcji `«ROUNDPD»`.

# [Instrukcja roundss](https://www.felixcloutier.com/x86/roundss)
# [Instrukcja comiss](https://www.felixcloutier.com/x86/comiss)
# [float.exposed](https://float.exposed/0x3f800000)

> **Rounding RC Field Description Mode Setting**
> - Round to **00B** Rounded result is the **closest to the infinitely precise result**. If two values are equally close, the result is nearest (even) the even value (i.e., the integer value with the least-significant bit of zero).
> - Round down **01B** Rounded result is closest to but no greater than the infinitely precise result. **(toward −∞)**
> - Round up **10B** Rounded result is closest to but no less than the infinitely precise result. **(toward +∞)**
> - Round toward **11B** Rounded result is closest to but no greater in absolute value than the infinitely precise result. zero **(Truncate)**

```assembly
puzzle9:        vmulss .LC2(%rip), %xmm0, %xmm6         ;x = a * 1/(2pi)
                vroundss $1, %xmm6, %xmm6, %xmm6        ;x = floor(a * 1/(2pi))
                vmulss .LC3(%rip), %xmm6, %xmm6         ;x = floor(a * 1/(2pi)) * 2pi
                vsubss %xmm6, %xmm0, %xmm6              ;x = a - 2pi * floor(a * 1/(2pi))
                vcomiss .LC4(%rip), %xmm6
                jb .L2                                  ;x < pi => jump L2
                vsubss .LC3(%rip), %xmm6, %xmm6         ;x -= 2pi
.L2:            vmovaps %xmm6, %xmm5                    ;power = x
                vmovaps %xmm6, %xmm0                    ;a = x
                vmovss .LC0(%rip), %xmm3                ;dbl_i = 2
                vmovss .LC1(%rip), %xmm4                ;factorial = 1
.L4:            vmovaps %xmm6, %xmm2                    ;tmp = x        
                vxorps .LC5(%rip), %xmm2, %xmm2         ;tmp = -x
                vmulss %xmm2, %xmm6, %xmm2              ;tmp = -x * x
                vmulss %xmm2, %xmm5, %xmm5              ;power *= -x * x
                vaddss .LC1(%rip), %xmm3, %xmm2         ;tmp = dbl_i + 1
                vmulss %xmm2, %xmm3, %xmm2              ;tmp = dbl_i * (dbl_i + 1)
                vmulss %xmm2, %xmm4, %xmm4              ;factorial *= dbl_i * (dbl_i + 1)
                vaddss .LC0(%rip), %xmm3, %xmm3         ;dbl_i += 2
                vdivss %xmm4, %xmm5, %xmm2              ;tmp = power / factorial
                vaddss %xmm2, %xmm0, %xmm0              ;a += power / factorial
                vandps .LC6(%rip), %xmm2, %xmm2
                vcomiss %xmm1, %xmm2
                ja .L4                                  ;vabs(power / factorial) > eps => jump L4
                ret                                     ;return a

.LC0:           .single 2.0
.LC1:           .single 1.0
.LC2:           .single 0.159154936                     ;1/(2*pi)
.LC3:           .single 6.283185482                     ;2*pi
.LC4:           .single 3.141592741                     ;pi
.LC5:           .long 0x80000000, 0, 0, 0               ;-0.0 (zapalony bit znaku, reszta zgaszona)
.LC6:           .long 0x7fffffff, 0, 0, 0               ;NaN (zapalone wszystkie bity poza bitem znaku)
```

```c
float sin(float a, float eps) {
    float x = a - (floorf(a * M_1_PI/2) * 2 * M_PI);    //przesunięcie a do przedziału [0, 2pi] 
    if (x >= M_PI) x -= 2*M_PI;                         //przesunięcie a do przedziału [-pi, pi]
    
    a = x;
    float power = x;
    float dbl_i = 2.0;
    float factorial = 1.0;

    do {
        power *= -x * x;
        factorial *= dbl_i * (dbl_i + 1.0);
        dbl_i += 2.0;
        a += power / factorial;
    } while (fabs(power / factorial) > eps)

    return a;
}
```

Funkcja ta liczy wartość $sin(a)$ z danym przybliżeniem $\epsilon$ wykorzystując [szereg Taylora](https://en.wikipedia.org/wiki/Sine_and_cosine#Series_definitions).