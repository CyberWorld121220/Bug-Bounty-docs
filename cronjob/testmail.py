#!/usr/bin/python3
import sys
import smtplib
# smtp (smtplib) is only for sending emails if you want to read email you must use imap or pop3
import easyimap as e
usermail = "bughuntertvaeneir@gmail.com"
password = "Family1024@"


# sending email
def send_email():
      server = smtplib.SMTP_SSL("smtp.gmail.com",465)
      server.login(usermail,password)
      server.sendmail("bughuntertvaeneir@gmail.com","viraj1024.1024@gmail.com","This is for Testing Purpose")
      #server.listids()
      server.quit()
# reading unread email => 
def read_email():
     server2 = e.connect("imap.gmail.com",usermail,password)
     #print(server2.listids())
     emailnum = len(server2.listids())
     #email = server2.mail(server2.listids()[1])
     #print(email.title)
     #print(email.from_addr)
     #print(email.attachments)
     #print(emailnum)
     i = 1
     while i <= emailnum :
        email = server2.mail(server2.listids()[i-1])
        #print(i)
        i = i + 1
        fullstring = str(email.title).strip()
        if "=>" in fullstring:
           target_output_name = str(email.title).strip().split("=>",1)[1]
           task = str(email.title).strip().split("=>",1)[0]
           print("task is :",task)
           print("target_output_name :",target_output_name)
           if task == "BugHunt":
               target = str(email.body).strip()
               print(str(email.body).strip())
               a = check_target(str(email.body).strip())
               #print(a)
               if a == None:
                  a = "attack"
               after_check(a,target)
           elif task == "PendingList":
              print("Showing Pending List...")
           elif task == "CompletedList":
              print("Showing Completed List...")
           else:
               return "OK"
        else:
           #print("No task given")
           return "No task given"
        
def check_target(target):
     file = open('completed.txt','r')
     Lines = file.readlines()
     count = 0
     completed = list()
     for line in Lines:
        count  +=1
        completed.append(line.strip())
     file.close()
     file = open('pending.txt','r')
     Lines = file.readlines()
     count = 0
     pending = list()
     for line in Lines:
        count  +=1
        pending.append(line.strip())
     file.close()
     pendingtest = 0
     attack = 0
     for l in completed:
        if l == target:
           return "completed"
           break
        else:
         #print("lets check for pending")
         pendingtest = 1
     for l in pending:
        if l == target:
           return "pending"
           break
        else:
           #print("lets start the attack..")
           attack = 1
     if attack == 1:
        return "attack"
def after_check(a,target):
   if a == "completed":
      print("Attack Completed alerady ...")
   elif a == "pending":
      print("Attack is still going....")
   elif a == "attack":
      print("lets lauch the attack")
      f = open("pending.txt","a")
      f.write(target+"\n")
      f.close()
      
   
#read_email()
send_email()
     
   

