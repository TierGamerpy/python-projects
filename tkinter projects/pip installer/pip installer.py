def pipthread():
    threa1=Thread(target=pip)
    threa1.start()

def pip():
    try:
        url=entry_.get()
        btn.configure(text='Loading..')
        btn.configure(state=DISABLED)
        vari=os.system(f'cmd/c"pip install {url}"')
        if vari == 0:
            messagebox.showinfo('Notification','Exist')
            btn.configure(text='INSTALL')
            btn.configure(state=NORMAL)
        else:
            btn.configure(text='INSTALL')
            btn.configure(state=NORMAL)
            messagebox.showerror('Notification','Unknown Option')
    except:
        btn.configure(text='INSTALL')
        btn.configure(state=NORMAL)
        messagebox.showerror('Notification','Unknown Option')

from tkinter import *
from tkinter import messagebox
import os
from threading import *

root = Tk()
root.title('PIP INSTALLER')
root.geometry('910x610+200+50')
root.resizable(False, False)

If = LabelFrame(root,text='Welcome To Pip Installer',font=('times' ,20, 'bold'),bd = 5,fg='blue',bg='#B9DDFC',relief=SUNKEN,labelanchor='n')
If.place(x=5,y=0,width=900,height=600)

titel_label=Label(If,text='Pip Install',font=('impact',40,'bold'),bg='#C6FD4F',fg='#D4B7F4')
titel_label.place(x=0,y=0,relwidth=1)

entry_ = Entry(If,font=('Arial',30,'bold'),bd=5,relief=SUNKEN,justify='center')
entry_.pack(pady=105)
entry_.focus()

btn=Button(If,text='INSTALL',font=('times',25,'bold'),bg='blue',fg='white',bd=5,cursor='hand2',command=pipthread)
btn.place(x=350,y=200)

root.mainloop()