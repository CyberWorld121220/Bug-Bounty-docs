#!/bin/bash
input="./completed.txt"
while IFS= read -r line
do
  echo "$line"
done < "$input"

