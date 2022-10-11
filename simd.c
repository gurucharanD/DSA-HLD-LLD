#include <stdio.h>
#include <smmintrin.h>
#include <immintrin.h>
#include <time.h>
#include <unistd.h>
#include <stdlib.h>

const int n = 262144;

void mult_vect(float *a, float *b)
{
    float c = 11.0;
    __m256 C = _mm256_broadcast_ss(&c);
    for (int i = 0; i < n; i += 8)
    {
        __m256 A = _mm256_load_ps(&a[i]);
        __m256 B = _mm256_mul_ps(A, C);
        _mm256_store_ps(&b[i], B);
    }
}

void mult_naive_code(float *a, float *b)
{
    float c = 11.0;
    for (int i = 0; i < n; i++)
    {
        b[i] = a[i] * c;
    }
}
void main()
{
    float a[n], b[n];
    float f[n], g[n];
    float c = 11.0;
    for (int i = 0; i < n; i++)
    {
        a[i] = 1.0;
        b[i] = 0.0;
        f[i] = 1.0;
        g[i] = 0.0;
    }
    clock_t start, end;
    double time_used = 0, time_used2 = 0;
    start = clock();
    mult_naive_code(a, b);
    end = clock();
    time_used = (double)(end - start) / CLOCKS_PER_SEC;
    printf("Time elapsed is %f seconds for naive multiplication \n", time_used);
    start = clock();
    mult_vect(f, g);
    end = clock();
    time_used2 = (double)(end - start) / CLOCKS_PER_SEC;
    printf(" Time elapsed is %f seconds for 256 bit vectorized multiplication\n", time_used2);
    printf(" Simd multiplicative vector is %f times faster than naive code of multiplication ", time_used / time_used2);
    printf("Hello world");
}
