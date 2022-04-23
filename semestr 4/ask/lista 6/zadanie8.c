__attribute__((noinline))
void for_range_do(long *cur, long *end, void (*fn)(long x)) {
    while(cur < end)
        fn(*cur++);
}

long sum(long *a, long n) {
    long res = 0;
    
    void accumulate(long x) {
        res += x;
    }

    for_range_do(a, a + n, accumulate);
    return res;
}