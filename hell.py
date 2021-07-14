import pyaudio
import speech_recognition as sr

r = sr.Recognizer()
mic = sr.Microphone(1)
with mic as source:
     r.adjust_for_ambient_noise(source)
     print("Please Speak :")
     audio = r.listen(source)
     print("Stop Talking")

     try:
         text = r.recognize_google(audio)
         print("You said : " + r. recognize_google(text))
     except:
         print("Sorry, I could not recognize what you said")