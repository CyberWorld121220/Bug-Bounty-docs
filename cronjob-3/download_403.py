#!/usr/bin/python3
from boto3.session import Session
import boto3
import os
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-d","--download",help="to download...")
args = parser.parse_args()
target = args.download
## creating session
access_key = 'AKIA6H52NPDKUVSQSCWJ'
secret_key = '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'
bucket = 'vps-s3-tvaeneir'
session = Session(aws_access_key_id=access_key,
              aws_secret_access_key=secret_key)
s3 = session.resource('s3')
your_bucket = s3.Bucket(bucket)
target_url = target+"/"+target+"_domain/list403-"+target+".txt"
print(target_url)
#save_as = target + "_tdir.txt"
your_bucket.download_file("evil.com/evil.com_domain/list403-evil.txt","evil.txt")
