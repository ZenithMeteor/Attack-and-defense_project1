#include <stdio.h>

int main(){
	char buf[100];
	printf("The buffer of your input %p\n",buf);
	puts("Can you pwn it ?");
	printf("Your input : ");
	fflush(stdout);
	gets(buf);
	puts("Goodbye ~");
	fflush(stdout);

}
