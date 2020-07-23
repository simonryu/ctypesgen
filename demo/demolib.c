/*
** Trivial ctypesgen demo library
**  from http://code.google.com/p/ctypesgen

Dumb manual build with:


    gcc -fPIC -c demolib.c
    gcc -shared -o demolib.so demolib.o

    gcc -fPIC -shared -o demolib.so demolib.c

*/

#include "demolib.h"
#include "stdio.h"


int trivial_add(int a, int b)
{
    return a + b;
}


double trivial_array_add(double** arr, int m, int n)
{
    printf("trivial_array_add \n");
    int i, j;
    double sum = 0.0;

    printf("before for-loop \n");
    printf("m: %d, n: %d \n", m, n);
    
    // for(i = 0;i < m*n;++i)
    //     printf("arr[%d]: %f \t", i, arr[i]);
    // printf("\n");

    for(i = 0;i < m;++i)
    {
        for(j = 0;j < n;++j)
        {
            sum += arr[i][j];
        }        
    }

    return sum;
}