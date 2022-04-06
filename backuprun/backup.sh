#!/bin/bash
cp /home/boxlogin/.bashrc /media/boxlogin/ExtraStuff1/Notes/backup-computer/bashrc.sh 
cp /root/.bashrc /media/boxlogin/ExtraStuff1/Notes/backup-computer/bashrc-root.sh
cp /media/boxlogin/ExtraStuff1/backuprun/backup.sh /media/boxlogin/ExtraStuff1/Notes/backup-computer/
cp /media/boxlogin/ExtraStuff1/Jarvis /media/boxlogin/ExtraStuff1/Notes/ -r
cp /home/boxlogin/Documents/term-banner.py /media/boxlogin/ExtraStuff1/Notes/backup-computer/
cp /home/boxlogin/vocabulary.txt  /media/boxlogin/ExtraStuff1/Notes/backup-computer/
cp /home/boxlogin/english.txt  /media/boxlogin/ExtraStuff1/Notes/backup-computer/
creds=`while read line;do echo $line;done < "/etc/creds/creds.txt"`
#cut=":"
IFS=":"
#read -d $cut -a strarr <<< $creds
read -ra strarr <<< $creds
index=${strarr[0]}
cipher="${strarr[1]}"
user="${strarr[2]}"
key=`echo $cipher | caesar $index`
echo $key
echo $user
cd /media/boxlogin/ExtraStuff1/Notes/;echo "`date`" > date.txt;git add -A;git commit -m "`date`";echo "${user}\n${key}" | git push "https://${user}:${key}@github.com/veer1024/Notes.git" master 
echo `date` > /home/boxlogin/lastgitbackup.txt
echo "last git backup" >> /home/boxlogin/lastgitbackup.txt
