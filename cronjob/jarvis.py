#!/usr/bin/python3
import sys
import smtplib
import pyttsx3
#speech recognizer
import speech_recognition as sr
# smtp (smtplib) is only for sending emails if you want to read email you must use imap or pop3
import easyimap as e
usermail = "bughuntertvaeneir@gmail.com"
password = "Family1024@"
listener = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # setting up new voice rate
#rate = engine.getProperty('rate')   # getting details of current speaking rate
#print (rate)
#volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
#print(volume)                          #printing current volume level
#voices = engine.getProperty('voices') 
engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1
#engine.setProperty('voice', voices[1].id)
def talk():
    engine.say("Hello Boss, this is Jarvis , what can i do for you ?")
    engine.runAndWait()
def talking(speech):
    engine.say(speech)
    engine.runAndWait()
def get_voice_instruction():
       try:
           with sr.Microphone() as source:
              print("listening...")
              listener.adjust_for_ambient_noise(source, duration=0.5)
              voice = listener.listen(source)
              info = listener.recognize_google(voice)
              #print(info)
              return info.lower()
       except sr.UnknownValueError:
              #talking("Sorry Boss , I did not get that")
              return "OK"
       except sr.RequestError:
              #talking("Sorry , my speech service is down")
              return "OK"

# sending email
def send_email():
      server = smtplib.SMTP_SSL("smtp.gmail.com",465)
      server.login(usermail,password)
      server.sendmail("Jarvis@gmail.com","viraj1024.1024@gmail.com","This is for Testing Purpose")
      #server.listids()
      server.quit()
# reading unread email => 
def read_email():
     server2 = e.connect("imap.gmail.com",usermail,password)
     print(server2.listids())
     email = server2.mail(server2.listids()[1])
     print(email.title)
     print(email.from_addr)
     print(email.attachments)

## this function is for analysing the voice command=>
def voicecommand(info):
     if "target" in info:
        talking("Locking Target to evil")
     else: 
        print(info)
   
#talk()
#send_email()
talking("hello boss")
talking("this is jarvis")
talking("what can i do")
talking("for you")
i = 1
while 0<1:
     print("command number: "+str(i))
     voice_command = get_voice_instruction()
     voicecommand(voice_command)
     print(voice_command)
     i = i + 1
