// gcc zadanie5.c zadanie5.s

#include <stdio.h>
#include <stdint.h>

uint32_t puzzle3(uint32_t, uint32_t);

int main () {
	for (uint32_t i = 1; i <= 50; i++) printf("%d/%d = %d == %d\n", 33, i, 33/i, puzzle3(33, i));
}