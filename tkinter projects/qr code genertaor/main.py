from tkinter import *
from tkinter import messagebox
import pyqrcode
import os

root = Tk()
root.geometry('570x400')
root.title('Qr Code Generator')
root.configure(bg='blue')
root.wm_iconbitmap(r'C:\Users\adity\Desktop\python projects\tkinter projects\qr code genertaor\Martz90-Circle-Qr-code.ico')
root.resizable(False, False)

#########################################################################functions

def Generate_Qr():
    Qr_Name = Qr_Name_Entry_Box.get()
    Qr_Id = Qr_Id_Entry_Box.get()
    Qr_Message = Qr_Message_Entry_Box.get()
    # print(Qr_Name,Qr_Id,Qr_Message)
    Message_Qr = 'Name : ' +Qr_Name+'\n'+'Id : '+Qr_Id+'\n'+'Qr_Message : '+Qr_Message 
    # print(Message_Qr)
    url = pyqrcode.create(Message_Qr)
    pp = r'C:\Users\adity\Desktop\python projects\qr code genertaor\qr codes'
    cc = '{}\{}{}.png'.format(pp,Qr_Id,Qr_Name)
    li = os.listdir(pp)
    if ('{}{}.png'.format(Qr_Id,Qr_Name) in li):
        messagebox.showinfo('Notification','Pls Choose Another Id Or Name..')
    else:
        url.png(cc,scale=5,)#module_color=(0,25,255,255),background=(0,255,25,255)
        mm = 'Qr Code Saved As : '+Qr_Id+Qr_Name+'.png'
        Qr_Notification_Message_Label.configure(text=mm)
        res = messagebox.askyesno('Notification','Qr Code Is Generated And Want To See It Then Yes :')
        if(res == True):
            top = Toplevel()
            top.geometry('400x400')
            top.configure(bg='white')
            img = PhotoImage(file=cc)
            label1 = Label(top,image=img,bg='white')
            label1.place(x=10,y=10)
            top.mainloop()
            


def Clear_Id_Name():
    Qr_Id_Entry_Box.delete(0,'end')
    Qr_Message_Entry_Box.delete(0,'end')
    Qr_Name_Entry_Box.delete(0,'end')
    Qr_Notification_Message_Label.configure(text='')

def Quit_root():
    res = messagebox.askokcancel('Notification','Are You Sure You Want To Quit ?')
    if res==True:
        root.destroy()
    else:
        pass

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
                            compound=RIGHT,command=Generate_Qr)
Generate_Qrimage_Button.place(x=10,y=250)

Clear_Id_Name_Button = Button(master=root,text='Clear',width=100,font=('times',10,'bold'),
                            bd=10,activebackground='blue',bg='powder blue',image=Clear_Id_Nameimage,
                            compound=RIGHT,command=Clear_Id_Name)
Clear_Id_Name_Button.place(x=210,y=250)

Quit_root_Button = Button(master=root,text='Quit',width=100,font=('times',10,'bold'),
                            bd=10,activebackground='blue',bg='powder blue',image=Quit_root_image,
                            compound=RIGHT,command=Quit_root)
Quit_root_Button.place(x=410,y=250)

######################################################################################hover effects
def Generate_Qrimage_ButtonEnter(e):
    Generate_Qrimage_Button['bg'] = 'purple2'
def Generate_Qrimage_ButtonLeave(e):
    Generate_Qrimage_Button['bg'] = 'powder blue'

def Clear_Id_Name_ButtonEnter(e):
    Clear_Id_Name_Button['bg'] = 'purple2'
def Clear_Id_Name_ButtonLeave(e):
    Clear_Id_Name_Button['bg'] = 'powder blue'

def Quit_root_ButtonEnter(e):
    Quit_root_Button['bg'] = 'purple2'
def Quit_root_ButtonLeave(e):
    Quit_root_Button['bg'] = 'powder blue'

Generate_Qrimage_Button.bind('<Enter>',Generate_Qrimage_ButtonEnter)
Generate_Qrimage_Button.bind('<Leave>',Generate_Qrimage_ButtonLeave)

Clear_Id_Name_Button.bind('<Enter>',Clear_Id_Name_ButtonEnter)
Clear_Id_Name_Button.bind('<Leave>',Clear_Id_Name_ButtonLeave)

Quit_root_Button.bind('<Enter>',Quit_root_ButtonEnter)
Quit_root_Button.bind('<Leave>',Quit_root_ButtonLeave)

#######################################################################################


root.mainloop()