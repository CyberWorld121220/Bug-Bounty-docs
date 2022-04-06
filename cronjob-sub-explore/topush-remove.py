#!/usr/bin/python3
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-p","--push",help="Push to remove...")
args = parser.parse_args()
target = args.push
## removing target from topush list
with open("TestingData/topush.txt", "r") as f:
         lines = f.readlines()
with open("TestingData/topush.txt", "w") as f:
      for line in lines:
         if line.strip("\n") != target:
            f.write(line)
