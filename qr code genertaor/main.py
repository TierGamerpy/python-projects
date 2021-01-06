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

Qr_Id_Entry_Box = Entry(master=root,width=25,bd=5,bg='pink',font=('times',17,'italic bold'),justify='center')
Qr_Id_Entry_Box.place(x=250,y=20)

Qr_Name_Entry_Box = Entry(master=root,width=25,bd=5,bg='pink',font=('times',17,'italic bold'),justify='center')
Qr_Name_Entry_Box.place(x=250,y=80)

Qr_Message_Entry_Box = Entry(master=root,width=25,bd=5,bg='pink',font=('times',17,'italic bold'),justify='center')
Qr_Message_Entry_Box.place(x=250,y=140)

#################################################################################### Buttons logos

Generate_Qrimage = PhotoImage(file='C:\\Users\\adity\\Desktop\\python projects\\qr code genertaor\\qr-code.png')
Generate_Qrimage = Generate_Qrimage.subsample(2,2)

Clear_Id_Nameimage = PhotoImage(file='C:\\Users\\adity\\Desktop\\python projects\\qr code genertaor\\eraser.png')
Clear_Id_Nameimage = Clear_Id_Nameimage.subsample(2,2)

Quit_root_image = PhotoImage(file='C:\\Users\\adity\\Desktop\\python projects\\qr code genertaor\\cancel.png')
Quit_root_image = Quit_root_image.subsample(2,2)

#################################################################################### Buttons

Generate_Qrimage_Button = Button(master=root,text='Generate',width=100,font=('times',10,'bold'),
                            bd=10,activebackground='blue',bg='powder blue',image=Generate_Qrimage,
                            compound=RIGHT)
Generate_Qrimage_Button.place(x=10,y=250)

Clear_Id_Name_Button = Button(master=root,text='Clear',width=100,font=('times',10,'bold'),
                            bd=10,activebackground='blue',bg='powder blue',image=Clear_Id_Nameimage,
                            compound=RIGHT)
Clear_Id_Name_Button.place(x=210,y=250)

Quit_root_Button = Button(master=root,text='Quit',width=100,font=('times',10,'bold'),
                            bd=10,activebackground='blue',bg='powder blue',image=Quit_root_image,
                            compound=RIGHT)
Quit_root_Button.place(x=410,y=250)

######################################################################################


root.mainloop()