#!/usr/bin/python3
import sys
import smtplib
# smtp (smtplib) is only for sending emails if you want to read email you must use imap or pop3
import easyimap as e
import os
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-t","--target",help="Target Completed...")
parser.add_argument("-p","--path",help="Path where to check...")
args = parser.parse_args()
target = args.target
path = args.path
## removing target from topush list
usermail = "jarvis.stark1024@gmail.com"
password = "Family1024@103267766"
password2 = "Family1024@"
tomail = "bughuntertvaeneir@gmail.com"
#msub = "BugHuntDir=>"+target
mbody = str(target).strip()
# sending Noneed email
def No_need(msub):
       server = smtplib.SMTP_SSL("smtp.gmail.com",465)
       server.login(tomail,password2)
       mhead = ['From:%s' % tomail, 'To:%s' %  usermail ,'Subject:%s' % msub]
       smsg = "\r\n\r\n".join(['\r\n'.join(mhead),mbody])
       server.sendmail(usermail, tomail, smsg)
       #server.listids()
       server.quit()

# sending email
def check_ready(path):
      Filenames = list()
      filename = "list403-"+target.split(".")[-2]+".txt"
      for l in next(os.walk(path))[2]:
          Filenames.append(l)
          #print(l)
      if filename in Filenames:
        #print("yes")
        send_email("BugHuntDir=>"+target)
      else:
        No_need("NoBugHuntDirNeed=>"+target)
      
def send_email(msub):
      server = smtplib.SMTP_SSL("smtp.gmail.com",465)
      server.login(usermail,password)
      mhead = ['From:%s' % usermail, 'To:%s' %  tomail ,'Subject:%s' % msub]
      smsg = "\r\n\r\n".join(['\r\n'.join(mhead),mbody])
      server.sendmail(usermail, tomail, smsg)
      #server.listids()
      server.quit()
#send_email()
check_ready(path)
