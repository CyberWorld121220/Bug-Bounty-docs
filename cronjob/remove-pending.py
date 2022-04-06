#!/usr/bin/python3
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-p","--pending",help="Pending Target to remove...")
args = parser.parse_args()
target = args.pending
with open("pending.txt", "r") as f:
    lines = f.readlines()
with open("pending.txt", "w") as f:
    for line in lines:
        if line.strip("\n") != target:
            f.write(line)
f = open("completed.txt","a")
f.write(target+"\n")
f.close()
