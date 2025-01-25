import re
from playsound import playsound
import eel
from engine.command import speak
from engine.config import ASSISTANT_NAME
import os
import pywhatkit as kit


@eel.expose
def playAssistantSound():   # Start PopUp Sound for Assistant
    music_dir = "frontend\\assets\\audio\\popup_sound.mp3"
    playsound(music_dir)


def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "")
    query.lower()

    if query!="":
        speak("Opening "+query)
        os.system('start '+query)
    else:
        speak("Sorry, I couldn't help with that.")

def playYoutube(query):
    searchTerm = extract_yt_term(query)
    speak("Playing "+searchTerm+" YouTube.")
    kit.playonyt(searchTerm)

def extract_yt_term(command):
    # Define a regular expression pattern to capture the song name
    pattern = r'play\s+(.*?)\s+youtube'
    # Use re.search() to find the match in command
    match = re.search(pattern, command, re.IGNORECASE)
    # If a match is found, return the extracted song name, ELSE retun none
    return match.group(1) if match else None
