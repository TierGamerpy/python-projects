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
root.config(bg='powder blue')
####################################################################################################labels
titel_Label = Label(root, text="Password Generator",bg='powder blue',fg='black',font=('arial',25, 'bold'))
titel_Label.pack(anchor='center',pady='20px')

Select_pass_length_label = Label(root, text="Select Your Password Length :- ",bg='powder blue',fg='green',font=('arial',12, 'bold'))
Select_pass_length_label.place(x='20px',y='85px')
##############################################################################################Selector
solidboss = IntVar()
passsword_Length_Selector = Combobox(root,textvariable=solidboss,state='readonly')
passsword_Length_Selector['values'] = [l for l in all_no.keys()]
passsword_Length_Selector.current(7)
passsword_Length_Selector.place(x='240px',y='85px')
##############################################################################################result label444
result_lable = Label(root, text="Generated Password Here :- ", bg='powder blue',fg='darkgreen',font=('arial',12,'bold'))
result_lable.place(x='20px',y='200px')

###############################################################################################final 
def password_generate():
    try:
        length_password = solidboss.get()
        small_letters = string.ascii_lowercase
        capital_letters = string.ascii_uppercase
        digits = string.digits
        special_character = string.punctuation
        all_list = []
        all_list.extend(list(small_letters))
        all_list.extend(list(capital_letters))
        all_list.extend(list(digits))
        all_list.extend(list(special_character))
        random.shuffle(all_list)
        password.set("".join(all_list[0:length_password]))
    except:
        messagebox.askretrycancel("A Problem Has Been Occured", "Please Try Again")

password= StringVar()
password_final = Entry(root , textvariable= password,state="readonly",fg='blue',font=('arial',15))
password_final.place(x='200px',y='200px')

##############################################################################################button genrate
generate_btn = Button(root, text="Genrate Password",bg='orange',fg='black',font=('arial',15),cursor='hand2',activebackground='blue',command=password_generate)
def on_enter(e):
    generate_btn['bg'] = 'red'
    generate_btn['fg'] = 'white'
def on_leave(e):
    generate_btn['bg'] = 'orange'
    generate_btn['fg'] = 'black'

generate_btn.bind('<Enter>',on_enter)
generate_btn.bind('<Leave>',on_leave)
generate_btn.pack(anchor='center',pady='65px')

##############################################################################################copy to clip board
def copytoclipboard():
    random_password = password.get()
    pyperclip.copy(random_password)

copy_Button = Button(root, text="Copy to clipboard",bg='orange',fg='black',font=('arial',15),cursor='hand2',activebackground='blue',command=copytoclipboard)
def on_enter_copy(e):
    copy_Button['bg'] = 'red'
    copy_Button['fg'] = 'white'
def on_leave_copy(e):
    copy_Button['bg'] = 'orange'
    copy_Button['fg'] = 'black'

copy_Button.bind('<Enter>',on_enter_copy)
copy_Button.bind('<Leave>',on_leave_copy)
copy_Button.place(x='125px',y='270px')

#############################################################################################
root.mainloop()