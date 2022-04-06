#!/usr/bin/python3
from boto3.session import Session
import boto3
import os
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-d","--download",help="to download...")
args = parser.parse_args()
target = args.download

## creating required directories =>
def create(path_target,target_dir):
    dirnames = list()
    for l in next(os.walk(path_target))[1]:
       dirnames.append(l)
    if target_dir in dirnames:
       return "main dir created already..."
    else: 
       os.mkdir(path_target+target_dir)
       return "going to create it "
## creating session
access_key = 'AKIA6H52NPDKUVSQSCWJ'
secret_key = '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'
bucket = 'vps-s3-tvaeneir'
session = Session(aws_access_key_id=access_key,
              aws_secret_access_key=secret_key)
s3 = session.resource('s3')
your_bucket = s3.Bucket(bucket)
global targetlist
targetlist = list()
filelist = list()
for s3_file in your_bucket.objects.all():
    #print(s3_file.key) # prints the contents of bucket
    filelist.append(s3_file.key)
    #print(s3_file[1])
# downloading the file from the bucket
#your_bucket.download_file(filelist[1], "./to/coinmetro.txt")
newlist = list()
for l in filelist:
   if l[0:len(target)] != None:
      if l[0:len(target)] == target:
        #print(l[0:len(target)])
        newlist.append(l)
      else:
        print("OUT OF SCOPE")
   else:
      print("OUT OF RANGE")
targetlist = newlist
filtered_list = list()
for l in targetlist:
   #print(l)
   a = l.split("/")
   #print(a[0])
   #print(len(a))
   #createdir(a)
   a.pop()
   filtered_list.append(tuple(a))
       
filtered_list = list(dict.fromkeys(filtered_list))
new_list = list()
for l in filtered_list:
   new_list.append(list(l))
#print(new_list)
for item in new_list:
  i = 0
  path = "./"
  while i < len(item):
      create(path,item[i])
      path = path + item[i]+"/"
      i = i + 1

## downloading the files and saving it to the repective directory =>
for l in newlist:
   #print(l)
   print(l)
   #print(l[-1])
   if l[-1] == "/":
      print("its a dir")
   else:
      your_bucket.download_file(l,l)





