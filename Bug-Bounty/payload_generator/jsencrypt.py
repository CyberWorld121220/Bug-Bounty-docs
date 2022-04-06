#!/usr/bin/python3
def encodejs(ascii):
     decimal_string = ""
     for char in ascii:
           decimal_string+= str(ord(char)) + ","
     return decimal_string[:-1]

input = input("Enter string to convert: ")
print(encodejs(input))
