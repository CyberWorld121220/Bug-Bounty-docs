import imaplib, email, smtplib, time, io

server = "imap.gmail.com"
fadd =  "bughuntertvaeneir@gmail.com"
mbody = ["""This is an example!"""]

while True:
    i = imaplib.IMAP4_SSL(server)
    i.login("bughuntertvaeneir@gmail.com", "Family1024@")
    i.list()
    i.select("INBOX")
    types, datas = i.search(None, "ALL")
    ids = datas[0]
    print(ids)
    if ids == "":
        i.logout()
        print("logout")
        pass
    else:
      print("Not logout")
      #id_list = ids.split() # ids is a space separated string
      #latest_email_id = id_list[-1] # get the latest
 
      #result, data = i.fetch(latest_email_id, "(RFC822)") # fetch the email body (RFC822) for the given ID
 
      #raw_email = data[0][1] # here's the body, which is raw text of the whole email
      #print(raw_email)
      # including headers and alternate payloads
      for n in ids.split():
          print("data is going to fetch")
          typs,dats = i.fetch(n, '(RFC822)')
          print("data is fetched now")
          for dat in dats:
            print("Start autoreply")
            if isinstance(dat, tuple):
	            
	            rmsg = email.message_from_string(dat[1].decode())
	            msub = rmsg['subject']
	            mfrom = rmsg['from'].replace("<", '').replace(">",'').split()[-1]
	            print(mfrom)
	            #print(mfrom,msub,rmsg)
	            if(mfrom == "test1@test.com") or (mfrom == "test2@test.com"):
	                pass
	            else:
	                mhead = ['From:%s' % fadd, 'To:%s' % mfrom ,'Subject:%s' % msub]
	                print("Sending Mail")		
	                smsg = "\r\n\r\n".join(['\r\n'.join(mhead), str(mbody[0]).strip()])
	                """
	                server2 = smtplib.SMTP()
	                server2.connect("smtp.gmail.com")
	                server2.starttls()
	                server2.login("bughuntertvaeneir@gmail.com", "Family1024@")
	                server2.sendmail(fadd, mfrom, smsg)
	                print ("Send to %s success!" % mfrom)
	                server.quit()
	                """
	                server2 = smtplib.SMTP_SSL("smtp.gmail.com",465)
	                server2.login("bughuntertvaeneir@gmail.com", "Family1024@")
	                server2.sendmail(fadd, mfrom, smsg)
	                server2.quit()
    time.sleep(120)
