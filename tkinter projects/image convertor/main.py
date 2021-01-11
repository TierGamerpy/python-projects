from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image
import os

win = Tk()
win.title('Image Convertor')
win.geometry('690x400+100+200')
win.resizable(False, False)
win.configure(bg='coral1')

titel_label=Label(win,text='Image Convertor',font='Arial 25 italic bold',
bg='brown',fg='white')
titel_label.place(x=0,y=0,relwidth=1)

choose_file=Label(win,text='Choose Photo',font='Arial 16 italic bold',
fg='white',bg='blue',relief=RIDGE)
choose_file.place(x=10,y=50)

entry_photo=Entry(win,font='arial 19 bold',width=26)
entry_photo.place(x=170,y=50)
entry_photo.focus()

#############################################################################################
def browsefile():
    file=filedialog.askopenfilename(title='Select Image',filetypes=(('.png','*.*'),('All files','*.*')))
    if(entry_photo==''):
        entry_photo.insert(0,file)
    else:
        entry_photo.delete(0,'end')
        entry_photo.insert(0,file)

btn_select_image=Button(win,text='Browse',font='Arial 11 bold',width=13,
bd=5,fg='white',bg='red',activebackground='brown',cursor='hand2',command=browsefile)
btn_select_image.place(x=544,y=47)

def btn_select_image_enter(e):
    btn_select_image['bg'] = 'green'
    btn_select_image['fg'] = 'white'
def btn_select_image_leave(e):
    btn_select_image['bg'] = 'red'
    btn_select_image['fg'] = 'white'

btn_select_image.bind('<Enter>', btn_select_image_enter)
btn_select_image.bind('<Leave>', btn_select_image_leave)
#############################################################################################

file_name=Label(win,text='File Name',font='Arial 16 italic bold',fg='white',bg='blue',relief=RIDGE,width=8)
file_name.place(x=10,y=120)
#############################################################################################

file_name_entry=Entry(win,font='Arial 19 bold',width=26)
file_name_entry.place(x=190,y=120)
########################################################################################################

file_type=Label(win,text='File Type',font='Arial 20 italic bold',fg='white',bg='blue',relief=RIDGE,width=8)
file_type.place(x=10,y=190)
#######################################################################################################

li = ['.png','.jpeg','.jpg','.ico','.pdf','.bmb']
com=StringVar()
combox = ttk.Combobox(win,width=25,font='Arial 19 bold',value=li,state='r',textvariable=com)
combox.place(x=190,y=190)
combox.set('Select Type')
#######################################################################################################
def converte_the_image():
    path = filedialog.askdirectory()
    path1 = entry_photo.get()
    path2 = file_name_entry.get()
    com_ = combox.get()
    save = path1 + com_
    if(path and path1 and path2):
        img=Image.open(path1)
        os.chdir(path)
        img.save(save)
    else:
        messagebox.showerror('Image Convertor','Fields Are Required')

convert_btn = Button(win,text='Convert The Iamge',font='Arial 18 bold',
bg='red',fg='white',activebackground='brown',cursor='hand2',bd=5,command=converte_the_image)
convert_btn.place(x=100,y=270)

def convert_btn_enter(e):
    convert_btn['bg'] = 'green'
    convert_btn['fg'] = 'white'
def convert_btn_leave(e):
    convert_btn['bg'] = 'red'
    convert_btn['fg'] = 'white'

convert_btn.bind('<Enter>', convert_btn_enter)
convert_btn.bind('<Leave>', convert_btn_leave)

#######################################################################################################
def reset():
    entry_photo.delete(0,'end')
    file_name_entry.delete(0,'end')
    combox.set('Select Type')

reset_btn = Button(win,text='Reset',font='Arial 18 bold',
bg='red',fg='white',activebackground='brown',cursor='hand2',bd=5,command=reset)
reset_btn.place(x=400,y=270)

def reset_btn_enter(e):
    reset_btn['bg'] = 'green'
    reset_btn['fg'] = 'white'
def reset_btn_leave(e):
    reset_btn['bg'] = 'red'
    reset_btn['fg'] = 'white'

reset_btn.bind('<Enter>', reset_btn_enter)
reset_btn.bind('<Leave>', reset_btn_leave)

win.mainloop()