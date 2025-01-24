import pyttsx3

def speak(text):    
    engine = pyttsx3.init('sapi5')
    
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id) # can be set between 0 and 2
    engine.setProperty('rate', 185) # speed of the AI speech command --- higher the number, faster the voice
    engine.setProperty('volume', 1.0) #between 0.0 and 1.0

    engine.say(text)
    engine.runAndWait()

speak("India is my country, all Indians are my brothers and sisters.")
