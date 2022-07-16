#import semua modul yang diperlukan
import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

#sebuah function untuk attach file
def attach_file(email_message, filename):
    with open(filename, "rb") as f:
        file_attachment = MIMEApplication(f.read())
    file_attachment.add_header(
        "Content-Disposition",
        f"attachment; filename={filename}",
    )
    email_message.attach(file_attachment)

#informasi email pengirim
email_from = 'emailpengirim'
email_pass = 'password'

#open file listemail untuk mendapatkan alamat email yang akan dituju
alamat = open('listemail.txt','r')
email_to=alamat.readlines()
alamat.close()

#menentukan subject email dan body email
email_message = MIMEMultipart('A')
email_message['Subject'] = 'Test Attachment' 
email_message['From'] = email_from
email_message['To'] = ','.join(email_to)
body_email = MIMEText("Hei!, semangat!")

#attach body email serta file ke pesan yang akan dikirim
email_message.attach(body_email)
attach_file(email_message, 'gambar.jpg')
email_string = email_message.as_string()

context=ssl.create_default_context() 

#mengirim email
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(email_from, email_pass)
    smtp.sendmail(email_from, email_to, email_string)

#daftar kode program
#https://www.youtube.com/watch?v=JRCJ6RtE3xU&list=LL&index=3&t=1034s
#https://www.programcreek.com/python/example/94019/email.mime.multipart.MIMEMultipart
#https://www.youtube.com/watch?v=NvtjLXSY-hE

