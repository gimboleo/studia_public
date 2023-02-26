#include <stdlib.h>
#include <stdbool.h>
#include <stdio.h>
#include <assert.h>
#include <math.h>

float swap(float* a, float* b)
{
    float temp = *a;
    *a = *b;
    *b = temp;
}

typedef struct Triangle
{
    float a, b, c;
} Triangle;

Triangle* Triangle_new(float a, float b, float c)
{
    if (a <= 0 || b <= 0 || c <= 0) return NULL;

    if (c > a) swap(&c, &a);
    if (c > b) swap(&c, &b);          //Po tej linii c to najmniejszy element
    if (b > a) swap(&b, &a);

    if (!(a < b + c)) return NULL;
    Triangle *newT = (Triangle *) malloc(sizeof(Triangle));
    newT->a = a;
    newT->b = b;
    newT->c = c;

    return newT;
}

bool is_triangle(struct Triangle *t)
{
    return t;
}

bool is_rectangular_triangle(struct Triangle *t)
{
    if(!t) return false;
    float res = (float) fabs(t->a * t->a - t->b * t->b - t->c * t->c);
    return (res < 0.0000001f);
}

bool is_equilateral_triangle(struct Triangle *t)
{
    if(!t) return false;
    return (t->a == t->b && t->b == t->c && t->c == t->a);
}

bool is_isosceles_triangle(struct Triangle *t)
{
    if(!t) return false;
    return (t->a == t->b || t->b == t->c || t->c == t->a);
}

int main()
{
    Triangle *test1 = Triangle_new(3, 4, 5);
    Triangle *test2 = Triangle_new(10, 10, 10);
    Triangle *test3 = Triangle_new(1, 2, 20);
    Triangle *test4 = Triangle_new(10, 10, 5);

    assert(is_triangle(test1));
    assert(!is_triangle(test3));

    assert(is_rectangular_triangle(test1));
    assert(!is_rectangular_triangle(test2));

    assert(is_equilateral_triangle(test2));
    assert(!is_equilateral_triangle(test4));

    assert(is_isosceles_triangle(test4));
    assert(!is_isosceles_triangle(test1));

    free(test1);
    free(test2);
    free(test3);
    free(test4);

    float a, b, c;
    scanf("%f %f %f", &a, &b, &c);

    Triangle *triangle = Triangle_new(a, b, c);

    printf("Triangle: %d\n", is_triangle(triangle));
    printf("Rectangular: %d\n", is_rectangular_triangle(triangle));
    printf("Equilateral: %d\n", is_equilateral_triangle(triangle));
    printf("Isoscles: %d\n", is_isosceles_triangle(triangle));
    if (triangle) free(triangle);

    return 0;
}