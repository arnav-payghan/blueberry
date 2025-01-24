import pyttsx3
import speech_recognition as sr


def speak(text):    
    engine = pyttsx3.init('sapi5')
    
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id) # can be set between 0 and 2
    engine.setProperty('rate', 185) # speed of the AI speech command --- higher the number, faster the voice
    engine.setProperty('volume', 1.0) #between 0.0 and 1.0

    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, 10, 6)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User Said: {query}")
    except Exception as e:
        return ""
    
    return query.lower() # gives output as text


text = takeCommand()

speak(text)
