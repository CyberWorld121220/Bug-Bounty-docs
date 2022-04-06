#!/usr/bin/python3
import sys
import smtplib
# smtp (smtplib) is only for sending emails if you want to read email you must use imap or pop3
import easyimap as e
global usermail
usermail = "bughuntertvaeneir@gmail.com"
global password
password = "Family1024@"
global tomail
tomail = "jarvis.stark1024@gmail.com"

def send_email(target,body):
      server = smtplib.SMTP_SSL("smtp.gmail.com",465)
      server.login(usermail,password)
      msub = body+"=>"+target
      mhead = ['From:%s' % usermail, 'To:%s' %  tomail ,'Subject:%s' % msub]
      smsg = "\r\n\r\n".join(['\r\n'.join(mhead), mbody])
      server.sendmail(usermail,tomail,smsg)
      #server.listids()
      server.quit()
