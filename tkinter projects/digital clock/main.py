from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title('Clock')
# root.maxsize(width='455',height='490')
# root.minsize(width='450',height='40')
root.iconbitmap(r'C:\Users\adity\Desktop\python projects\digital clock\Iconsmind-Outline-Clock-2.ico')

def time():
    string = strftime('%H:%M:%S %p')
    label.configure(text=string)
    label.after(1000, time)

label = Label(root,font=('ds-digital',80),background='black',foreground='cyan')
label.pack(anchor='center')
time()

mainloop()