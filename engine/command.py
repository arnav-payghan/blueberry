import pyttsx3
import speech_recognition as sr
import eel
import time


def speak(text):    
    engine = pyttsx3.init('sapi5')
    
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id) # can be set between 0 and 2
    engine.setProperty('rate', 185) # speed of the AI speech command --- higher the number, faster the voice
    engine.setProperty('volume', 1.0) #between 0.0 and 1.0

    eel.displayMessage(text)

    engine.say(text)
    engine.runAndWait()

@eel.expose
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        eel.displayMessage("Listening")
        r.pause_threshold = 2.5
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, 10, 10)

    try:
        print("Recognizing")
        eel.displayMessage("Recognizing")
        query = r.recognize_google(audio, language="en-in")
        print(f"User Input: {query}")
        eel.displayMessage(query)
        time.sleep(3)
    except Exception as e:
        return ""
    
    return query.lower() # gives output as text

#text = takeCommand()
#speak(text)

@eel.expose()
def allCommands():
    try:

        ### OPENING FEATURES
        query = takeCommand()
        print(query)

        if "open" in query:
            from engine.features import openCommand
            openCommand(query)
        elif "on youtube" in query:
            from engine.features import playYoutube
            playYoutube(query)

        ### WHATSAPP FEATURES    
        

        ### END FEATURE
        else:
            print("Nothing Error 101: Please check the code or the command.")
    except:
        print("Error")
        
    
    eel.showHood()
