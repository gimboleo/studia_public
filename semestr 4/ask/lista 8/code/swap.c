extern int printf(const char *, ...);
extern int buf[];

int *bufp0 = &buf[0];
static int *bufp1;
static float sum = 0.0;

static void incr() {
  static int count = 0;
  count++;
}

void addf(float x) {
  sum += x + 3.14;
  printf("sum = %f\n", sum);
}

void swap() {
  int temp;
  incr();
  bufp1 = &buf[1];
  temp = *bufp0;
  *bufp0 = *bufp1;
  *bufp1 = temp;
}
