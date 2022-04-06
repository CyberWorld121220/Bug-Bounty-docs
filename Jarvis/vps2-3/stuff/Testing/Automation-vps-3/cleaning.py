#!/usr/bin/python3
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-f","--file",help="file to clean...")
parser.add_argument("-o","--output",help="output name...")
args = parser.parse_args()
file = args.file
output = args.output
f = open(file,"r")
o = open(output+".txt","a")
lines = f.readlines()
lines.pop(0)
for line in lines:
   linedata = line.split(",")
   print(linedata)
   print(linedata[-1])
   a = int(linedata[-1].strip())
   print(a)
   if a > 0:
     o.write(linedata[0]+" ===>>> "+linedata[1]+" --->>> "+linedata[-1]+"\n")
   else:
     print(linedata[0]+" ===>>>has nothing to search ")
print("Cleaning Done")
