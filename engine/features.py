import re
import sqlite3
import struct
import eel
import os
import pywhatkit as kit
import webbrowser
import pyaudio
import pvporcupine 
import pyautogui as autogui

from playsound import playsound
from engine.command import speak
from engine.config import ASSISTANT_NAME
from engine.helper import extract_yt_term



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


def hotword():
    purcupine = None
    paud = None
    audio_stream = None
    try:
        # PRE TRAINED KEYWORDS
        porcupine = pvporcupine.create(keywords=["hex", "nova"])
        paud = pyaudio.PyAudio()
        audio_stream = paud.open(rate=porcupine.sample_rate, channels=1, format=pyaudio.paInt16, input=True, frames_per_buffer=porcupine.frame_lenght)

        # LOOP FOR STREAMING
        while True:
            keyword = audio_stream.read(porcupine.frame_length)
            keyword = struct.unpack_from("h" * porcupine.frame_length, keyword)
            # processing keyword comes from mic
            keyword_index = porcupine.process(keyword)
            # checking first keyword detected or not
            if keyword_index >= 0:
                print("Hotword Detected")
                # pressing shortcut with "H" using autogui
                autogui.keyPress("H")
    except:
        if porcupine is not None:
            porcupine.delete()
        if audio_stream is not None:
            audio_stream.close()
        if paud is not None:
            paud.terminate()
