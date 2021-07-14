import pyttsx3
import datetime
import speech_recognition as sr 
import wikipedia
import webbrowser
import os, sys, subprocess
import smtplib

def open_file(filename):
    if sys.platform != "win32":
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, filename])
        #os.startfile(filename)
    else:
        os.startfile(filename)
        #opener = "open" if sys.platform == "darwin" else "xdg-open"
        #subprocess.call([opener, filename])


engine = pyttsx3.init('nsss')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

#def startfile(fn):
 #   os.system('open %s' % fn)
def open_file(filename):
    if sys.platform != "win32":
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, filename])
        #os.startfile(filename)
    else:
        os.startfile(filename)
        #opener = "open" if sys.platform == "darwin" else "xdg-open"
        #subprocess.call([opener, filename])


def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jarvis Sir. Please tell me how may I help you") 





def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source,duration=1)
        print("what")
        audio = r.listen(source)
        print("hi") 

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n") 

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
    #if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            url = 'https://www.wikipedia.org/'
            chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
            webbrowser.get(chrome_path).open(url)
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, "sentences=2")
            speak("According to Wikipedia")
            print(results)
            speak(results)

        #correct
        elif 'open youtube' in query:
            url = 'https://www.youtube.com/'
            chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
            webbrowser.get(chrome_path).open(url)

        #correct
        elif 'open google' in query:
            #webbrowser.open("google.com")
            url = 'https://www.google.co.in/'
            chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
            webbrowser.get(chrome_path).open(url)

        #correct
        elif 'play music' in query:
            url = 'https://wynk.in/music/playlist/weekly-top-20-english/bb_1527140401220'
            chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
            webbrowser.get(chrome_path).open(url)
            #music_dir = '/Users/adityagoyal/Documents/GitHub/Project_Jarvis/Code/bensound-ukulele.wav'
            
            #songs = os.listdir(music_dir)
            #print(songs)    
            #subprocess.run(music_dir, shell=True)
            #os.chdir()
           # os.system( "//Users//adityagoyal//Documents//GitHub//Project_Jarvis//Code//bensound-ukulele.wav" )
            #os.startfile(os.path.join(music_dir, songs[0]))
        
        #correct
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        #correct
        elif 'open safari' in query:
            url = 'https://www.google.co.in/'
            safari_path = "open -a /Applications/Safari.app %s"
            webbrowser.get(safari_path).open(url)
        
        elif 'email to aditya' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "adityagoyal204@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend aditya. I am not able to send this email")
