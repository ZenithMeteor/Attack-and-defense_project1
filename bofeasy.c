#include <stdio.h>

void l33t() {
    puts("Congrat !!Congrat");
    system("/bin/sh");
}

int main() {
    char buf[20];
    puts("Buffer overerflow is easy");
    printf("Read your input :");
    fflush(stdout);
    read(fflush0,buf,100);
    return 0 ;
}
