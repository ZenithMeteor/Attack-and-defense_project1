#include <stdio.h>
#include <stdlib.h>
#define BUF_SIZE 50

int fp = 0;
char name[BUF_SIZE] = {'0'};

int main()
{
	char buffer[BUF_SIZE];
	fp = open("/home/bssfp/fake", 'r');

	puts("User name:");

	scanf("%s", name);
	printf("\n");

	read(fp, buffer, BUF_SIZE);

	if (!strncmp(buffer, name, BUF_SIZE))
	{
		printf("Good!\n");
		system("cat /home/bssfp/flag");
	}

	else
	{
		printf("User does not exist.\n");
	}

	return 0;
}
