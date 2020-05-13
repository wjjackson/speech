### speech recognizer 

import speech_recognition as sr

r = sr.Recognizer()

with sr.AudioFile('/Users/will/Documents/python/speech/harvard.wav') as source:
    audio = r.record(source)

print(r.recognize_google(audio))
