#include <stdio.h>

char name[200];
char *filename;

int main(){
	FILE *fp ;
	char buf[2704];
	puts("What's your name ?");
	fflush(stdout);
	filename = "/home/bssof/welcome";
	gets(name);
	fp = fopen(filename,"r");
	if(!fp){
		puts("Error !!");
		return -1;
	}else{
		fread(buf,2704,1,fp);
	}
	printf("%s\n",buf);
	printf("Goodbye ~ %s\n",name);
	fflush(stdout);
	return 0 ;
}
