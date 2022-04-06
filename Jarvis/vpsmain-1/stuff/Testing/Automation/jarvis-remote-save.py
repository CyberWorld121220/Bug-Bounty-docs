#!/usr/bin/python3
import os
global filelist
import shutil
filelist = list()
target_path = "/media/boxlogin/ExtraStuff1/hunt/PenTest"
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
        #client_s3.put_object(Bucket=bucket, Key=(folder_name+'/'))
        print(target + " 1")
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
            #client_s3.upload_file(item,bucket,item)
            os.system("cp -r "+target+" "+target_path)
            print(item)
            #shutil.copyfile(item,target_path)
            print(item + " 2")
            print("item not found: ",item)
            f = open(target+".txt","a")
            f.write(item+"\n")
            f.close()
    #print(client_s3)
    f = open('s3-presently.txt','w')
    f.write("NotWorking"+"\n")
    f.close()
if ready_to_work():
    ## creating connection to bucket
    global client_s3
    access_key = 'AKIA6H52NPDKUVSQSCWJ'
    secret_key = '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'
    bucket = 'vps-s3-tvaeneir'
    #client_s3 = boto3.client('s3',aws_access_key_id=access_key,aws_secret_access_key=secret_key)
    check_for_new_upload()
    #print("Ready")
else:
    print("Rest!")
