#!/usr/bin/python3
import os
import boto3
access_key = 'AKIA6H52NPDKUVSQSCWJ'
secret_key = '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'
bucket = 'vps-s3-tvaeneir'
#folder_name = "testing"
global filelist
filelist = list()
## listing files inside the target
def getting_files_path(target_path):
     Filenames = list()
     Dirnames = list()
     for l in next(os.walk(target_path))[2]:
          Filenames.append(l)
     for l in next(os.walk(target_path))[1]:
          Dirnames.append(l)
     for f in Filenames:
         path = target_path+f
         filelist.append(path)
     for d in Dirnames:
         path = target_path+d+"/"
         getting_files_path(path)


def ready_to_work():
     file = open('s3-presently.txt','r')
     Lines = file.readlines()
     state = list()
     count = 0
     for line in Lines:
       count +=1
       state.append(line.strip())
     file.close()
     #print(state[0])
     file = open('topush.txt','r')
     string = file.read()
     #print(string.strip())
     #print(len(string.strip()))
     if len(string.strip()) >= 1:
        if state[0] == "working":
           return False
        else:
           return True
     else:
       return False
## check for any new data to upload =>
def check_for_new_upload():
     file = open('topush.txt','r')
     Lines = file.readlines()
     count = 0
     topush = list()
     for line in Lines:
        count  +=1
        topush.append(line.strip())
     file.close()
     for target in topush:
        folder_name = target
        client_s3.put_object(Bucket=bucket, Key=(folder_name+'/'))
        upload(target)
def upload(target):
    f = open(target+".txt","a")
    f.close()
    targetdir = target+"/"
    getting_files_path(targetdir)
    print(filelist)
    file = open(target+".txt",'r')
    Lines = file.readlines()
    count = 0
    uploaded = list()
    for line in Lines:
         count  +=1
         uploaded.append(line.strip())
    file.close()
       ## now uploading for file started
    for item in filelist:
         if item in uploaded:
            print("item found: ",item)
            
         else:
            client_s3.upload_file(item,bucket,item)
            print("item not found: ",item)
            f = open(target+".txt","a")
            f.write(item+"\n")
            f.close()
    #print(client_s3)
    f = open('s3-presently.txt','w')
    f.write("NotWorking"+"\n")
    f.close()
## listing files present in a folder
"""
Uloading files to bucket
"""
#client_s3.upload_file("./test",bucket,"test")
#folder_name = "name/ofyour/folders"
#arr = os.listdir(".")
#print(arr)
"""
dir = "./"
print (next(os.walk(dir))[1])
print (next(os.walk(dir))[2])
for l in next(os.walk(dir))[1]:
     print(l)
getting_files_path("./testing.com/")
print(filelist)
"""
#upload("testing.com")
#client_s3.put_object(Bucket=bucket, Key=(folder_name+'/'))
if ready_to_work():
    ## creating connection to bucket
    global client_s3
    access_key = 'AKIA6H52NPDKUVSQSCWJ'
    secret_key = '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'
    bucket = 'vps-s3-tvaeneir'
    client_s3 = boto3.client('s3',aws_access_key_id=access_key,aws_secret_access_key=secret_key)
    check_for_new_upload()
    #print("Ready")
else:
    print("Rest!")


