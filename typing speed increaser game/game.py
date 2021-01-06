import random
from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('800x600+400+100')
root.configure(bg='powder blue')
root.title('Typind Speed Increaser Game')
root.iconbitmap('C:\\Users\\adity\\Desktop\\python projects\\typing speed increaser game\\logo.ico')

########################################################################################


words = [
    'mango',
    'apple',
    'gun',
    'door',
    'help',
    'kite',
    'monitor',
    'banana',
    'orange',
    'buffalo',
    'laptop'.
    'mouse',
    'key',
    'phone',
    'dekstop'
]

score = 0
timeleft = 60
count = 0
sliderWords = ''
miss = 0

#########################################################


def labelSlider():
    global count,sliderWords
    text = 'Welcome To Typing Speed Increaser Game'
    if (count >= len(text)):
        count = 0
        sliderWords = ''
    sliderWords += text[count]
    count += 1
    fontLabel.configure(text=sliderWords)
    fontLabel.after(150,labelSlider)

def time():
    global timeleft,score,miss
    if timeleft >=11:
        pass
    else:
        timeLabelCount.configure(fg='red')
    if timeleft >0:
        timeleft -= 1
        timeLabelCount.configure(text=timeleft)
        timeLabelCount.after(1000,time)
    else:
        gamePlayDetailLabel.configure(text=f'Hit = {score} | Miss = {miss} | Total Score = {score-miss}')
        rr = messagebox.askretrycancel('Notification','To Play Again Hit Retry Button')
        if rr==True:
            score = 0
            timeleft = 60
            miss = 0
            timeLabelCount.configure(text=timeleft)
            wordLabel.configure(text=words[0])
            scoreLabelCount.configure(text=score)
            timeLabelCount.configure(fg='blue')

def startGame(event):
    global score,miss
    if timeleft == 60:
        time() 
    gamePlayDetailLabel.configure(text='')
    if(wordEntry.get() == wordLabel['text']):
        score += 1
        scoreLabelCount.configure(text=score)
        # print('Score: ',score)
    else:
        miss += 1
        # print('Miss: ',Miss)
    random.shuffle(words)
    wordLabel.configure(text=words[0])
    wordEntry.delete(0,END)


###########################################################################################


fontLabel = Label(root,text='',font=('airal',25,'italic bold'),bg='powder blue',fg='red',width=40)
fontLabel.place(x=10,y=10)
labelSlider()

random.shuffle(words)
wordLabel = Label(root,text=words[0],font=('airal',40,'italic bold'),bg='powder blue')
wordLabel.place(x=350,y=200)

scoreLabel = Label(root,text='Your Score : ',font=('airal',25,'italic bold'),bg='powder blue')
scoreLabel.place(x=10,y=100)

scoreLabelCount = Label(root,text=score,font=('airal',25,'italic bold'),bg='powder blue',fg='blue')
scoreLabelCount.place(x=80,y=180)

timerLabel = Label(root,text='Time Left : ',font=('airal',25,'italic bold'),bg='powder blue')
timerLabel.place(x=600,y=100)

timeLabelCount = Label(root,text=timeleft,font=('airal',25,'italic bold'),bg='powder blue',fg='blue')
timeLabelCount.place(x=680,y=180)

gamePlayDetailLabel = Label(root,text='Type Word And Hit Enter Button',font=('airal',30,'italic bold'),bg='powder blue',fg='dark grey')
gamePlayDetailLabel.place(x=120,y=450)


##################################################################################################################################


wordEntry = Entry(root,font=('airal',25,'italic bold'),bd=10,justify='center')
wordEntry.place(x=250,y=300)
wordEntry.focus_set()

###########################################################################


root.bind('<Return>',startGame)

########################################################################################

root.mainloop()