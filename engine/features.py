import re
import sqlite3
from playsound import playsound
import eel
from engine.command import speak
from engine.config import ASSISTANT_NAME
import os
import pywhatkit as kit
import webbrowser

conn = sqlite3.connect("assistant.db")
cursor = conn.cursor()

@eel.expose
def playAssistantSound():   # Start PopUp Sound for Assistant
    music_dir = "frontend\\assets\\audio\\popup_sound.mp3"
    playsound(music_dir)


def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "")
    query.lower()

    app_name = query.strip()

    if app_name != "":
        try:
            cursor.execute('SELECT path FROM sys_command WHERE name IN (?)', (app_name,))
            results = cursor.fetchall()

            if len(results) != 0:
                speak("Opening "+ query)
                os.startfile(results[0][0])
            elif len(results) == 0:
                cursor.execute('SELECT url FROM web_command WHERE name IN (?)', (app_name,))
                results = cursor.fetchall()

                if len(results) != 0:
                    speak("Opening "+query)
                    webbrowser.open(results[0][0])
                else:
                    speak("Opening "+query)
                    try:
                        os.system('start '+query)
                    except:
                        speak("Not Found")
        except:
            speak("Something went wrong.")           

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
