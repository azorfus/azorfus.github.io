#include <stdio.h>
#include <stdlib.h>

int main()
{
    unsigned long seed = 0;
	printf("Enter seed: ");
	scanf("%lu", &seed);
	// Seed the random number generator with 100
	srand(seed);

	unsigned long A = rand();
	unsigned long B = rand();

	printf("Solution for pin 2: %lu\n", A);

	int a, b, c, d;

	d = 0x66666667;
	c = B;
	a = c;
	d = ((long long int) d * a >> 32);
	d = d >> 2;
	a = c;
	a = a >> 0x1f;
	d = d - a;
	a = d;
	a = a << 0x2;
	a = a + d;
	a = a + a;
	c = c - a;
	d = c;
	a = d + 0x41; // G value
	printf("G: 0x%x\n", a);

	return 0;
}
