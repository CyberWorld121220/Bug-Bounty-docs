#! /bin/bash

# Given string 
string="Lelouch,Akame,Kakashi,Wrath"

# Setting IFS (input field separator) value as ","
IFS=','

# Reading the split string into array
read -ra arr <<< "$string"

# Print each value of the array by using the loop
for val in "${arr[@]}";
do
  printf "name = $val\n"
done
