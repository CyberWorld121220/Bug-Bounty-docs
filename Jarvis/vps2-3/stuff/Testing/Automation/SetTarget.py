#!/usr/bin/python3
import sys
import smtplib
# smtp (smtplib) is only for sending emails if you want to read email you must use imap or pop3
import easyimap as e
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-t","--target",help="Target to attack...")
parser.add_argument("-r","--remove",help="Target remove confirmation from complete list...")
parser.add_argument("-s","--refresh",help="Frefreshing the Instance...")
args = parser.parse_args()
if args.target != None:
    target = args.target
else:
    target = "state"
## removing target from topush list
usermail = "jarvis.stark1024@gmail.com"
password = "Family1024@103267766"
tomail = "bughuntertvaeneir@gmail.com"
msub = "BugHunt=>"+target
msubremove = "CompletedRemove=>"+target
msubremovep = "PendingRemove=>"+target
msubrefresh = "Refresh=>refresh"
mbody = str(target).strip()
# sending email
def send_email():
      if args.refresh == "yes":
        server = smtplib.SMTP_SSL("smtp.gmail.com",465)
        server.login(usermail,password)
        mhead = ['From:%s' % usermail, 'To:%s' %  tomail ,'Subject:%s' % msubrefresh]
        smsg = "\r\n\r\n".join(['\r\n'.join(mhead), mbody])
        server.sendmail(usermail, tomail, smsg)
        #server.listids()
        server.quit()
      if args.remove == None and args.refresh != "yes":
        server = smtplib.SMTP_SSL("smtp.gmail.com",465)
        server.login(usermail,password)
        mhead = ['From:%s' % usermail, 'To:%s' %  tomail ,'Subject:%s' % msub]
        smsg = "\r\n\r\n".join(['\r\n'.join(mhead), mbody])
        server.sendmail(usermail, tomail, smsg)
        #server.listids()
        server.quit()
      else:
        server = smtplib.SMTP_SSL("smtp.gmail.com",465)
        server.login(usermail,password)
        mhead = ['From:%s' % usermail, 'To:%s' %  tomail ,'Subject:%s' % msubremove]
        smsg = "\r\n\r\n".join(['\r\n'.join(mhead), mbody])
        server.sendmail(usermail, tomail, smsg)
        #server.listids()
        server.quit()
        server = smtplib.SMTP_SSL("smtp.gmail.com",465)
        server.login(usermail,password)
        mhead = ['From:%s' % usermail, 'To:%s' %  tomail ,'Subject:%s' % msubremovep]
        smsg = "\r\n\r\n".join(['\r\n'.join(mhead), mbody])
        server.sendmail(usermail, tomail, smsg)
        #server.listids()
        server.quit()
send_email()
f = open('pull.txt','a')
f.write(target)
f.close()
