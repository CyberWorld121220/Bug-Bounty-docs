// Program to implement atoi() in C
#include <stdio.h>
 
// A simple atoi() function
int myAtoi(char* str)
{
    // Initialize result
    int res = 0;
 
    // Iterate through all characters
    // of input string and update result
    // take ASCII character of corresponding digit and
    // subtract the code from '0' to get numerical
    // value and multiply res by 10 to shuffle
    // digits left to update running total
    for (int i = 0; str[i] != '\0'; ++i)
        res = res * 10 + str[i] - '0';
 
    // return result.
    return res;
}
 
// Driver Code
int main()
{
    char str[] = "viraj";
   
    // Function call
    int val = myAtoi(str);
    printf("%d ", val);
    return 0;
}
