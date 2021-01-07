from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
import string
import random
import pyperclip
####################################################################################################
all_no = {
'1' : '1',
'2' :'2',
'3':'3',
'4':'4',
'5':'5',
'6':'6',
'7':'7',
'8':'8',
'9':'9',
'10':'10',
'11':'11',
'12':'12',
'13':'13',
'14':'14',
'15':'15',
'16':'16',
'17':'17',
'18':'18',
'19':'19',
'20':'20',
'21':'21',
'22':'22',
'23':'23',
'24':'24',
'25':'25',
'26':'26',
'27':'27',
'28':'28',
'29':'29',
'30':'30'
}

####################################################################################################
root = Tk()
root.title('Password Generator')
root.iconbitmap(r'C:\Users\adity\Desktop\python projects\tkinter projects\password generator\Iconsmind-Outline-Password-Field.ico')
root.geometry("500x500")
root.resizable(False, False)
root.config(bg='beige')
####################################################################################################labels
titel_Label = Label(root, text="Password Generator",bg='beige',fg='black',font=('arial',15, 'bold'))
titel_Label.pack(anchor='center',pady='20px')

Select_pass_length_label = Label(root, text="Select Your Password Length :- ",bg='beige',fg='green',font=('arial',12, 'bold'))
Select_pass_length_label.place(x='20px',y='70px')
##############################################################################################Selector
solidboss = IntVar()
passsword_Length_Selector = Combobox(root,textvariable=solidboss,state='readonly')
passsword_Length_Selector['values'] = [l for l in all_no.keys()]
passsword_Length_Selector.current(7)
passsword_Length_Selector.place(x='240px',y='70px')
##############################################################################################button
generate_btn = Button(root, text="Genrate Password",bg='orange',fg='black',font=('arial',15),cursor='hand2')
def on_enter(e):
    generate_btn['bg'] = 'grey'
    generate_btn['fg'] = 'white'
def on_leave(e):
    generate_btn['bg'] = 'orange'
    generate_btn['fg'] = 'black'

generate_btn.bind('<Enter>',on_enter)
generate_btn.bind('<Leave>',on_leave)
generate_btn.pack(anchor='center',pady='50px')


root.mainloop()