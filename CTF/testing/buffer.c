#include <err.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
char *gets(char *);
void abracadabra() {  
 printf("Success..! Function called :D\n");  
 exit(0);  
}
int main(int argc, char **argv) {  
 struct {  
 char buffer[64];  
 volatile int (*point)();  
 } hackvist;  
  
 hackvist.point = NULL;  
 gets(hackvist.buffer);  
  
 if (hackvist.point) {  
 printf("Function Pointer → %p\n", hackvist.point);  
 fflush(stdout);  
 hackvist.point();  
 } else {  
 printf("Try Again\n");  
 }  
  
 exit(0);  
}
