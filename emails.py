#import semua modul yang diperlukan
import os, smtplib, ssl
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

def menu():
    flag = 0
    while(flag!=1) :
        print("------------Menu-------------")
        print("1. Ganti Email Pengirim")
        print("2. Tambahkan Email Penerima")
        print("3. Edit Isi Email")
        print("4. Kirim Email")
        print("5. Tentang Program")
        print("6. Keluar Program")
        pilih = input('Pilih menu : ')
        try:
            int(pilih)
            flag = 1
        except:
            print("Mohon masukan menu berupa angka!")
    return int(pilih)

def menu_edit():
    listfile=[]
    subject = input("Tuliskan Subject baru   : ")

    return subject, listfile, bodyEmail



def main():
    email_from = os.environ.get('email_from')
    email_pass = os.environ.get('email_password')

    alamat = open('listemail.txt','r')
    email_to=alamat.readlines()
    alamat.close()

    email_message = MIMEMultipart('A')
    subject = 'Test Attachment' 
    email_message['From'] = email_from
    email_message['To'] = ','.join(email_to)
    body = MIMEText("Hei!, semangat!")
    listfile=['gambar.jpg', 'listemail.txt']

    pilihan = menu()
    while(pilihan!=6):
        if pilihan==1:
            pass
        elif pilihan==2:
            pass
        elif pilihan==3:
            subject=input('Masukan Subject : ')
            listfile.clear()
            lagi='ya'
            while(lagi.lower()=='ya'):
                namafile =input("Masukan nama file       : ")
                listfile.append(namafile)
                lagi=input("Masukan file baru? [ya/tidak]: ")
            body=input("Masukan Body EMail baru : ")
            pass
        elif pilihan==4:
            email_message = MIMEMultipart('A')
            email_message['Subject'] = subject 
            email_message['From'] = email_from
            email_message['To'] = ','.join(email_to)
            body_email = MIMEText(body)
            email_message.attach(body_email)
            for f in listfile:
                attach_file(email_message, f)
            email_string = email_message.as_string()

            context=ssl.create_default_context() 

            #mengirim email
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
                smtp.login(email_from, email_pass)
                smtp.sendmail(email_from, email_to, email_string)
            
        elif pilihan==5:
            pass
        elif pilihan==6:
            break
        else:
            print("Menu yang Anda pilih tidak tersedia!")
        pilihan=menu()

main()
os.system('pause')
exit()

#informasi default
#informasi email pengirim
email_from = os.environ.get('email_from')
email_pass = os.environ.get('email_password')

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

