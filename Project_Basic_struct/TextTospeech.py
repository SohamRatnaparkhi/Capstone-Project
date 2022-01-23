from gtts import gTTS
from playsound import playsound
import win32com
from win32com import client
import os

audio = 'speech.mp3'
language = 'en'
sentence = input("What you want to convert :- ")
choice = input("Do you want a male voice or a female voice ? (M/F) ")
choice = choice.lower()
speaker = win32com.client.Dispatch("SAPI.SpVoice")
if choice == 'f':
    sp = gTTS( text = sentence, lang = language, slow = False )
    sp.save(audio)
    playsound(audio)  
elif choice == 'm':
    sp = speaker.Speak(sentence)
    

    

