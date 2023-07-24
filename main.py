from tkinter import *
import socket
#import time
from tkinter import filedialog
from tkinter import messagebox
import os

from rsa_integrated import *

root=Tk()
root.title("Transferrrr")
root.geometry("350x400+500+200")
root.configure(bg="#856ff8")
root.resizable(False,False)

def Send():
    window=Toplevel(root)
    window.title("Sender")
    window.geometry("300x280+500+200")
    window.configure(bg='Violet')
    window.resizable(False,False)


    def select_file():
        global filename
        filename=filedialog.askopenfilename(initialdir=os.getcwd(),
                                            title="Select File",
                                            filetype=(('file_type','*.txt'),('all files',".*")))
        print(filename)

    def ss():
        s=socket.socket()
        host=socket.gethostname()
        port=8080
        s.bind((host,port))
        s.listen(1)
        print(host)
        print("WAITING FOR ANY INCOMING CONNECTIONS.........!")
        conn,addr=s.accept()
        p1=int(input("Enter key1:"))
        q1=int(input("Enter key2:"))
        r1=int(input("Enter key3:"))
        temp = filename.split("/")
        #start = time.time()
        file = encrypt_rsa(p1,q1,r1,temp[len(temp)-1])
        #end = time.time()
        print(file)
        conn.send(file.encode())
        print("DATA TRANSMITTED SUCCESSFULLY......!")
        #print("Time taken for data encryption:",(end - start))
        
    #icon
    image_icon1=PhotoImage(file="D:/studies/CN project final/icon_file.png")
    window.iconphoto(False,image_icon1)

    Button(window,text="select file to send",width=14,height=1,font='arial 14 bold',bg='White',fg='Black',command=select_file).place(x=60,y=30)
    Button(window,text="SEND",width=7,height=1,font='arial 14 bold',bg="White",fg='Black',command=ss).place(x=110,y=100)

    host=socket.gethostname()
    Label(window,text=f'ID:{host}',width=15,height=1,bg='white',fg='black').place(x=100,y=180)
    window.mainloop()

def Receive():
    main=Toplevel(root)
    main.title("receiver")
    main.geometry("430x350+500+200")
    main.configure(bg='Violet')
    main.resizable(False,False)

    def rer():
        ID=SenderID.get()
        filename1=incoming_file.get()
        temp = filename1.split("/")
        temp = temp[len(temp)-1]
        s=socket.socket()
        port=8080
        s.connect((ID,port))
        file_data=s.recv(200000)
        file_data = file_data.decode()
        print(file_data)
        p2=int(input("Enter key1:"))
        q2=int(input("Enter key2:"))
        r2=int(input("Enter key3:"))
        #start = time.time()
        Res = rsa_decrypt(p2,q2,r2,file_data)
        #end = time.time()
        file=open(temp,'w')
        file.write(Res)
        file.close()
        print("FILE HAS BEEN RECEIVED SUCCESSFULLY........!")
        #print("Time taken for decryption:",(end-start))
    
    #icon
    image_icon1=PhotoImage(file="D:/studies/CN project final/icon_file.png")
    main.iconphoto(False,image_icon1)

    Label(main,text='Receive',font=('arial',20),bg='White',fg='Black').place(x=150,y=50)

    Label(main,text='Input sender id',font=('arial',10,'bold'),bg='White',fg='Black').place(x=30,y=100)
    SenderID=Entry(main,width=25,fg='Black',border=2,bg='White',font=('arial',15))
    SenderID.place(x=30,y=150)
    SenderID.focus()

    Label(main,text='Filename for incoming file:',font=('arial',10,'bold'),bg='White',fg='Black').place(x=30,y=190)
    incoming_file=Entry(main,width=25,fg='Black',border=2,bg='White',font=('arial',15))
    incoming_file.place(x=30,y=240)
    
    rr=Button(main,text='Receive',compound=LEFT,bg='White',fg='Black',font='arial 14 bold',command=rer)
    rr.place(x=320,y=250)
    
    main.mainloop()
    
#icon
image1=PhotoImage(file="D:/studies/CN project final/icon_file.png")
root.iconphoto(False,image1)

Label(root,text="File Transfer",font=('Acumin Variable Concept',20),bg="#856ff8").place(x=90,y=9)
Label(root,text='Transferrrr-A file transfer app created by Bharathi.M',font=('Acumin Variable Concept',10),bg="#856ff8").place(x=25,y=327)
Label(root,text='124157008',font=('Acumin Variable Concept',8),bg='#856ff8').place(x=140,y=350)
Frame(root,width=400,height=2,bg="#f3f5f6").place(x=0,y=45)

#send button
send=Button(root,text="SEND",bg="pink",bd='5',command=Send)
send.place(x=50,y=65)

#receive button
receive=Button(root,text="RECEIVE",bg="pink",bd='5',command=Receive)
receive.place(x=225,y=65)

Label(root,image=image1).place(x=50,y=105)
root.mainloop()