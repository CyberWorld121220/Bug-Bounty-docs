#include <stdio.h>
int main() {
    vuln();
}

int vuln()         // function definition   
{
      int number = 0;
    char whoareyou[60];
    //char flag = "";
    printf("number: 0\n");
    printf("whoareyou: unknown\n");
    printf("Can you overwrite the value of number to something else?, btw what is your name: ");
    gets(whoareyou);
    
    // true if number is less than 0
    if (number) {
        puts("Congrats you have successfully overwrited the value of number,your flag is N&S{blahblahblah}");
        //printf("");
    }
    else{
        printf("Hey %s\n",whoareyou);
        puts("value of number is not changed yet, try again...");
    }

    //printf("The if statement is easy.");

    return 0;
}
