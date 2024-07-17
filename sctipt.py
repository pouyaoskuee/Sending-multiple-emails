import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from time import sleep


youremail= "your82@gmail.com"
yourpas= 'your pass'

server= smtplib.SMTP("smtp.gmail.com",587,timeout=3600)
server.starttls()
server.ehlo()
server.login(youremail,yourpas)

emails = open("emails.txt")
emails = emails.read()
emails = emails.split('\n')
massage="hi"
for i in emails:
    msg = MIMEMultipart()
    msg["subject"] = "your email subgect"
    msg["from"] = youremail
    msg["to"] = i
    msg.attach(MIMEText(massage))
    server.sendmail(youremail,i,msg.as_string())
    print(f"email was seccsessfully sent to :{i}")
    sleep(2)