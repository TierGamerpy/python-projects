import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# wishing me and 
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak('Good Morning,Sir')
    elif hour >=12 and hour<15:
        speak('Good Afternoon,Sir')
    else:
        speak('Good Evening,Sir')
    speak('I am Jarvis sir. How Can i help you')

# taking input voice
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening.....')
        r.pause_threshold = 0.8
        # r.energy_threshold = 300
        audio = r.listen(source)

    try:
        print('Recognizing....')
        query = r.recognize_google(audio, language='en-in')
        print(f'User Said: {query}\n')

    except Exception as e:
        print(e)
        print('Say That Again Please...')
        return 'None'
    return query

if __name__ == '__main__':
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

    # logic for excuting tasks based on query
    # wikipedia search
        if 'search wikipedia' in query:
            speak('Searching Wikipedia....')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query,sentences=2)
            speak('According to wikipedia')
            # print(results)
            speak(results)
        # # google search command
        # elif 'search' in query:
        #     webbrowser.open('https://www.google.com/search?q='+query)
        #     speak('searching sir')
            # youtbe opening
        elif 'open youtube' in query:
            speak('Opening Youtube')
            webbrowser.open('https://www.youtube.com')
            # google opening
        elif 'open google' in query:
            speak('Opening google')
            webbrowser.open('https://www.google.com')
            # github opening
        elif 'open github' in query:
            speak('Opening github')
            webbrowser.open('https://www.github.com')
            # gmail opening
        elif 'open gmail' in query:
            speak('Opening gmail')
            webbrowser.open('https://www.gmail.com')
        # whats the time
        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime('%I:%M %p')
            print(f'The Time Is {strTime}')
            speak(f'Sir,The Time Is {strTime}')
        # elif 'what is the date' in query:
        #     strTime = datetime.datetime.now().strftime('%H:%M:%S')
        #     print(f'The Time Is {strTime}')
        #     speak(f'Sir,The Time Is {strTime}')
        # openning vs ocde
        elif 'open code' in query:
            codepath = "D:\\program files\\Microsoft VS Code\\Code.exe"
            speak('opening vs code')
            os.startfile(codepath)
        # openning sublime
        elif 'open sublime' in query:
            codepath = "D:\\program files\\Sublime Text 3\\sublime_text.exe"
            speak('opening sublime text editor')
            os.startfile(codepath)
        # sying hi  
        elif 'hi jarvis' in query:
            speak('hello sir')
        # sying hello
        elif 'hello jarvis'  in query:
            speak('hello sir')
     