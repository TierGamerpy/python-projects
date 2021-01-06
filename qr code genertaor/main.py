from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('570x400')
root.title('Qr Code Generator')
root.configure(bg='blue')
root.wm_iconbitmap('C:\\Users\\adity\\Desktop\\python projects\\qr code genertaor\\Martz90-Circle-Qr-code.ico')
####################################################################### labels

Qr_Id_Label = Label(master=root,text='Enter Your Id : ',bg='powder blue',fg='red',width=20,height=2,
                    font=('times',12,'italic bold'))
Qr_Id_Label.place(x=10,y=20)

Qr_Name_Label = Label(master=root,text='Enter Your Name : ',bg='powder blue',fg='red',width=20,height=2,
                    font=('times',12,'italic bold'))
Qr_Name_Label.place(x=10,y=80)

Qr_Message_Label = Label(master=root,text='Enter Your Message : ',bg='powder blue',fg='red',width=20,height=2,
                    font=('times',12,'italic bold'))
Qr_Message_Label.place(x=10,y=140)

Qr_Notification_Label = Label(master=root,text='Notification : ',bg='powder blue',fg='red',width=10,height=2,
                    font=('times',15,'italic bold underline'))
Qr_Notification_Label.place(x=10,y=350)

Qr_Notification_Message_Label = Label(master=root,text='',bg='powder blue',fg='red',width=30,height=2,
                    font=('times',15,'bold'))
Qr_Notification_Message_Label.place(x=200,y=350)

################################################################################ entry boxes

Qr_Id_Entry_Box = Entry(master=root,width=25,bd=5,bg='pink',font=('times',17,'italic bold'))
Qr_Id_Entry_Box.place(x=250,y=20)

Qr_Name_Entry_Box = Entry(master=root,width=25,bd=5,bg='pink',font=('times',17,'italic bold'))
Qr_Name_Entry_Box.place(x=250,y=80)

Qr_Message_Entry_Box = Entry(master=root,width=25,bd=5,bg='pink',font=('times',17,'italic bold'))
Qr_Message_Entry_Box.place(x=250,y=140)

#################################################################################### Buttons logos


#################################################################################### Buttons

Generate_Qrimage_Button = Button(master=root,text='Generate',width=15,font=('times',10,'bold'),
                            bd=10,activebackground='blue',bg='powder blue')
Generate_Qrimage_Button.place(x=10,y=250)

Clear_Id_Name_Button = Button(master=root,text='Clear',width=15,font=('times',10,'bold'),
                            bd=10,activebackground='blue',bg='powder blue')
Clear_Id_Name_Button.place(x=210,y=250)

Quit_root_Button = Button(master=root,text='Quit',width=15,font=('times',10,'bold'),
                            bd=10,activebackground='blue',bg='powder blue')
Quit_root_Button.place(x=410,y=250)

######################################################################################


root.mainloop()