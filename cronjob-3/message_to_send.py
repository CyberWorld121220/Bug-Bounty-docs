#!/usr/bin/python3
import sys
import smtplib
# smtp (smtplib) is only for sending emails if you want to read email you must use imap or pop3
import easyimap as e
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-t","--target",help="Target Completed...")
parser.add_argument("-m","--message",help="Message to Send...")
args = parser.parse_args()
target = args.target
message = args.message
## removing target from topush list
tomail = "jarvis.stark1024@gmail.com"
password = "Family1024@"
usermail = "bughuntertvaeneir@gmail.com"
msub = "Status=>"+target
text = str(target).strip() + " : "+ str(message).strip()
mbody = text
# sending email
def send_email():
      server = smtplib.SMTP_SSL("smtp.gmail.com",465)
      server.login(usermail,password)
      mhead = ['From:%s' % usermail, 'To:%s' %  tomail ,'Subject:%s' % msub]
      smsg = "\r\n\r\n".join(['\r\n'.join(mhead), mbody])
      server.sendmail(usermail, tomail, smsg)
      #server.listids()
      server.quit()
send_email()
