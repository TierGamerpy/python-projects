from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
from textblob import TextBlob
root= Tk()
root.geometry('500x400')
root.resizable(False, False)
root.configure(bg='powder blue')
root.iconbitmap(r'C:\Users\adity\Desktop\python projects\tkinter projects\text translator\Treetog-Junior-Earth.ico')

####################################################################################
lan_dict = {'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar', 'armenian': 'hy', 'azerbaijani': 'az', 'basque': 'eu', 'belarusian': 'be', 'bengali': 'bn', 'bosnian': 'bs', 'bulgarian': 'bg', 'catalan': 'ca', 'cebuano': 'ceb', 'chichewa': 'ny', 'chinese (simplified)': 'zh-cn', 'chinese (traditional)': 'zh-tw', 'corsican': 'co', 'croatian': 'hr', 'czech': 'cs', 'danish': 'da', 'dutch': 'nl', 'english': 'en', 'esperanto': 'eo', 'estonian': 'et', 'filipino': 'tl', 'finnish': 'fi', 'french': 'fr', 'frisian': 'fy', 'galician': 'gl', 'georgian': 'ka', 'german': 'de', 'greek': 'el', 'gujarati': 'gu', 'haitian creole': 'ht', 'hausa': 'ha', 'hawaiian': 'haw', 'hebrew': 'he', 'hindi': 'hi', 'hmong': 'hmn', 'hungarian': 'hu', 'icelandic': 'is', 'igbo': 'ig', 'indonesian': 'id', 'irish': 'ga', 'italian': 'it', 'japanese': 'ja', 'javanese': 'jw', 'kannada': 'kn', 'kazakh': 'kk', 'khmer': 'km', 'korean': 'ko', 'kurdish (kurmanji)': 'ku', 'kyrgyz': 'ky', 'lao': 'lo', 'latin': 'la', 'latvian': 'lv', 'lithuanian': 'lt', 'luxembourgish': 'lb', 'macedonian': 'mk', 'malagasy': 'mg', 'malay': 'ms', 'malayalam': 'ml', 'maltese': 'mt', 'maori': 'mi', 'marathi': 'mr', 'mongolian': 'mn', 'myanmar (burmese)': 'my', 'nepali': 'ne', 'norwegian': 'no', 'odia': 'or', 'pashto': 'ps', 'persian': 'fa', 'polish': 'pl', 'portuguese': 'pt', 'punjabi': 'pa', 'romanian': 'ro', 'russian': 'ru', 'samoan': 'sm', 'scots gaelic': 'gd', 'serbian': 'sr', 'sesotho': 'st', 'shona': 'sn', 'sindhi': 'sd', 'sinhala': 'si', 'slovak': 'sk', 'slovenian': 'sl', 'somali': 'so', 'spanish': 'es', 'sundanese': 'su', 'swahili': 'sw', 'swedish': 'sv', 'tajik': 'tg', 'tamil': 'ta', 'telugu': 'te', 'thai': 'th', 'turkish': 'tr', 'ukrainian': 'uk', 'urdu': 'ur', 'uyghur': 'ug', 'uzbek': 'uz', 'vietnamese': 'vi', 'welsh': 'cy', 'xhosa': 'xh', 'yiddish': 'yi', 'yoruba': 'yo', 'zulu': 'zu'}
#########################################################################
def entry1_on_enter(e):
    entry1['bg'] = 'springgreen'
def entry1_on_leave(e):
    entry1['bg'] = 'white'

varname1 = StringVar()
entry1=Entry(root,width=30,textvariable=varname1,font='times 15 italic bold')
entry1.place(x=150,y=40)

entry1.bind('<Enter>',entry1_on_enter)
entry1.bind('<Leave>',entry1_on_leave)
####################################################################################
def entry2_on_enter(e):
    entry2['bg'] = 'springgreen'
def entry2_on_leave(e):
    entry2['bg'] = 'white'

varname2 = StringVar()
entry2=Entry(root,width=30,textvariable=varname2,font='times 15 italic bold')
entry2.place(x=150,y=100)

entry2.bind('<Enter>',entry2_on_enter)
entry2.bind('<Leave>',entry2_on_leave)
#########################################################################
label1=Label(root,text='Enter Word',font='times 15 italic bold',bg='powder blue')
label1.place(x=5,y=40)

label2=Label(root,text='Translated',font='times 15 italic bold',bg='powder blue')
label2.place(x=5,y=100)

label3=Label(root,text='',font='times 15 italic bold',bg='powder blue')
label3.place(x=10,y=250)
#########################################################################
def btn1_on_enter(e):
    btn1['bg'] = 'springgreen'
def btn1_on_leave(e):
    btn1['bg'] = 'yellow'

def tt():
    word3 = TextBlob(varname1.get())
    lan = word3.detect_language()
    lan_todict = languages.get()
    lan_to = lan_dict[lan_dict]
    word3 = word3.translate(from_lang=lan,to=lan_to)
    label3.configure(text=word3)

imgbt1 = PhotoImage(file=r'C:\Users\adity\Desktop\python projects\tkinter projects\text translator\clicking.png')
imgbt1.subsample(2,2)

btn1=Button(root,text='Click',bd=10,bg='yellow',activebackground='red',width=100,font='times 15 italic bold',
image=imgbt1,compound=RIGHT,command= tt)
btn1.place(x=70,y=170)
btn1.bind('<Enter>',btn1_on_enter)
btn1.bind('<Leave>',btn1_on_leave)

#########################################################################
def btn2_on_enter(e):
    btn2['bg'] = 'springgreen'
def btn2_on_leave(e):
    btn2['bg'] = 'yellow'

def main_exit():
    rr = messagebox.askyesnocancel('Notification','Are You Want To Exit?',parent=root)
    if rr == True:
        root.destroy()
    if rr == False:
        pass
    else:
        pass

imgbt2 = PhotoImage(file=r'C:\Users\adity\Desktop\python projects\tkinter projects\text translator\logout.png')
imgbt2.subsample(2,2)

btn2=Button(root,text='Exit',bd=10,bg='yellow',activebackground='red',width=100,font='times 15 italic bold',
image=imgbt2,compound=RIGHT,command=main_exit)
btn2.place(x=280,y=170)
btn2.bind('<Enter>',btn2_on_enter)
btn2.bind('<Leave>',btn2_on_leave)

#########################################################################

languages = StringVar
font_box = Combobox(root,width=30,textvariable=languages,state='r')
font_box['values'] = [e for e in lan_dict.keys()]
font_box.current(37)
font_box.place(x=300,y=0)

#########################################################################
root.mainloop()