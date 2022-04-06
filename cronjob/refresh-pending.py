#!/usr/bin/python3
with open("pending.txt", "r") as f:
    lines = f.readlines()
with open("completed.txt", "a") as f:
    for line in lines:
        f.write(line)
