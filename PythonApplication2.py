from msilib.schema import File
from stat import FILE_ATTRIBUTE_SPARSE_FILE
from tkinter import *
import email
import smtplib,ssl
from email.message import EmailMessage
import imghdr
from tkinter import filedialog


file="utka.png"
def vali_pilt():
    global file
    file=filedialog.askopenfilename()
    return file



def saada_kiri():
    kellele=email_box.get()  #komu
    kiri=kiri_box.get("1.0", END) #chto
    smtp_server="smtp.gmail.com"
    port=587
    sender_email="tthkmaks@gmail.com"  #komu otpravit
    password="hnsm ksgm nvvc txtz"   #input()
    context=ssl.create_default_context()
    msg=EmailMessage()
    msg.set_content(kiri)
    msg['Subject']="E-kiri saatmine"  #from Entry
    msg['From']="Maksim Stjopin"
    msg['To']=kellele
    with open("utka.png",'rb') as fpilt:
        pilt=fpilt.read()
    msg.add_attachment(pilt,maintype="image",subtype=imghdr.what(None,pilt))
    try:
        server=smtplib.SMTP(smtp_server,port)
        server.starttls(context=context)
        server.login(sender_email,password)
        server.send_message(msg)
        # polzovatel znal chto otpravil pismo
    except Exception as e:
        print() #tkinter
    finally:
        server.quit()


aken=Tk()
aken.geometry("400x300")
aken.title("TKinter. Zagolovok")
aken.iconbitmap("scary.ico")

l_mail=Label(aken,text="Email",bg="#df4f4f",fg="#efcf6f",font="Castellar 20",height=1,width=8)
l_kiri=Label(aken,text="Kiri",bg="#df4f4f",fg="#efcf6f",font="Castellar 20",height=1,width=8)
l_mail.grid(row=0, column=0)
l_kiri.grid(row=1, column=0)

email_box=Entry(aken,fg="#df4f4f",bg="#efcf6f",font="Arial 20",width=20,justify=LEFT)
email_box.grid(row=0, column=1, columnspan=2)

kiri_box=Text(aken,fg="#df4f4f",bg="#efcf6f",font="Arial 20",height=6,width=20)
kiri_box.grid(row=1, column=1,columnspan=2)

saada_btn=Button(aken,text="Saada",bg="blue",font="Arial 12",relief=GROOVE,command=saada_kiri)
saada_btn.grid(row=2, column=2)

pilt_btn=Button(aken,text="Pilt",bg="blue",font="Arial 12",relief=GROOVE,command=saada_kiri)
pilt_btn.grid(row=2, column=1)



netu nihuja okna!!!






aken.mainloop() 