#daftar kode program dan daftar pustaka
#https://www.youtube.com/watch?v=JRCJ6RtE3xU&list=LL&index=3&t=1034s
#https://www.programcreek.com/python/example/94019/email.mime.multipart.MIMEMultipart
#https://www.youtube.com/watch?v=NvtjLXSY-hE

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

def send_email(email_from, email_pass, email_to, listfile, email_message, body, subject):
            email_message = MIMEMultipart()
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
            #email akan berhasil dikirim jika username dan password yang dimasukan (jika memilih menu1) cocok, jika tidak pesan error akan ditampilkan
            try : 
                with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
                    smtp.login(email_from, email_pass)
                    smtp.sendmail(email_from, email_to, email_string)
                print("Email berhasil dikirim!")
                flag=1
            except:
                print("Error! Pastikan username dan password yang Anda masukan benar!")
                flag=0
            return flag

def tambah_email(email_to):
    #menambahkan email baru ke list email yang telah tersedia
    #email baru tidak akna dimasukan ke dalam file listemail
        lagi='ya'
        while(lagi.lower()=='ya'):
            tambahemail=input("Masukan email penerima    : ")
            email_to.append(tambahemail)
            lagi=input("Masukan email baru? [ya/tidak]: ")
        return email_to

def tambah_file(listfile):
    #menambahkan file baru ke list file yang telah tersedia
    #file baru tidak akna dimasukan ke dalam file listefile
        lagi='ya'
        while(lagi.lower()=='ya'):
            namafile =input("Masukan nama file       : ")
            listfile.append(namafile)
            lagi=input("Masukan file baru? [ya/tidak]: ")
        return listfile

def main():
    #nilai default
    email_from = os.environ.get('email_from')
    email_pass = os.environ.get('email_password')
    alamat = open('listemail.txt','r')
    email_to=alamat.readlines()
    alamat.close()
    email_message = MIMEMultipart()
    subject = 'Hello, there!' 
    body = "hei semangatss!"
    listfile=['gambar.jpg', 'listemail.txt']
#-------------------------------------------------------
    pilihan = menu()
    while(pilihan!=6):
        if pilihan==1:
            #mengganti email_from dan email_pass
            email_from = input('Masukan email pengirim : ')
            email_pass = input('Password               : ')
            pass
        elif pilihan==2:
            #memanggil function tambah_email untuk menambahkan email baru ke list penerima email
            email_to = tambah_email(email_to)
        elif pilihan==3:
            #mengganti subject, body, dan file attachment (dengan memanggil function tambah_file)
            subject=input('Masukan Subject         : ')
            listfile = tambah_file(listfile)
            body=   input("Masukan Body EMail baru : ")
        elif pilihan==4:
            #mengirimkan email dengan memanggil function send_email
            send = send_email(email_from, email_pass, email_to, listfile, email_message, body, subject)
            #jika ditemukan ketidak cocokan antara username dan password yang dimasukan, email_from dan email_pass akan diubah kembali ke bentuk default
            if send == 0:
                email_from = os.environ.get('email_from')
                email_pass = os.environ.get('email_password')
        elif pilihan==5:
            #membuka file tentang.txt yang berisi penjelasan singkat program
            tentang=open('tentang.txt','r')
            print(tentang.read())
        elif pilihan==6:
            break
        else:
            print("Menu yang Anda pilih tidak tersedia!")
        os.system('pause')
        os.system('cls')
        pilihan=menu()

main()
os.system('cls')
print("\n\n\t\t~Terima Kasih~\n\n")
exit()