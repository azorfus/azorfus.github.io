#include <stdio.h>
#include <unistd.h>
#include <string.h>

/*
int main (int argc, char** argv) {

    char buf[40];
	printf("Buffer: %p\n", &buf);
    strcpy(buf, argv[1]);
    printf("%s\n", buf);

    return 0;
}
*/

int main()
{
	char buffer[40];
	printf("Buffer: %p\n", &buffer); // For debugging purposes
	gets(buffer);
	printf(buffer);

	return 0;
}
