import re
import sqlite3
import struct
import subprocess
import time
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
from engine.helper import extract_yt_term, remove_words
from shlex import quote


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
    porcupine = None
    paud = None
    audio_stream = None
    try:
        # PRE TRAINED KEYWORDS
        porcupine = pvporcupine.create(keywords=["blueberry", "grapefruit", "jarvis"])
        paud = pyaudio.PyAudio()
        audio_stream = paud.open(rate=porcupine.sample_rate, channels=1, format=pyaudio.paInt16, input=True, frames_per_buffer=porcupine.frame_length)

        # LOOP FOR STREAMING
        while True:
            keyword = audio_stream.read(porcupine.frame_length, exception_on_overflow=False)
            keyword = struct.unpack_from("h" * porcupine.frame_length, keyword)
            # processing keyword comes from mic
            keyword_index = porcupine.process(keyword)
            # checking first keyword detected or not
            if keyword_index >= 0:
                print("Hotword Detected")
                # pressing shortcut with "H" using autogui
                autogui.keyDown("win")
                autogui.press("j")
                time.sleep(2)
                autogui.keyUp("win")
    except:
        if porcupine is not None:
            porcupine.delete()
        if audio_stream is not None:
            audio_stream.close()
        if paud is not None:
            paud.terminate()
        print("Error blueberry: unable to start the hotword detection")


### FINDIG CONTACTS FUNCTION
def findContact(query):
    words_to_remove = [ASSISTANT_NAME, 'make', 'a', 'to', 'phone', 'call', 'send', 'message', 'whatsapp', 'video']
    query = remove_words(query, words_to_remove)

    try:
        query = query.strip().lower()
        cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
        results = cursor.fetchall()
        print(results[0][0])
        mobile_number_str = str(results[0][0])
        if not mobile_number_str.startswith('+91'):
            mobile_number_str = '+91' + mobile_number_str
            return mobile_number_str, query
    except:
        speak('Does Not Exists in Contact List')
        return 0, 0


def whatsApp(mobile_no, message, flag, name):
    if flag == 'message':
        target_tab = 12
        blueberry_message = "Message sent successfully to " + name
    elif flag == 'phone call':
        target_tab = 6
        message = ''
        blueberry_message = "Calling " + name
    elif flag == 'video call':
        target_tab = 5
        message = ''
        blueberry_message = "Video Calling " + name
    
    ### ENCODING THE MESSAGE FOR URL
    encoded_message = quote(message)
    ### CONSTRUCT THE URL
    whatsapp_url = f"whatsapp://send?phone={mobile_no}&text={encoded_message}"
    ### CONSTRUCT THE FULL COMMAND
    full_command = f'start "" "{whatsapp_url}"'
    ### OPENING WHATSAPP USING THE CONSRUCTED URL USING CMD.EXE
    subprocess.run(full_command, shell=True)
    time.sleep(5)
    subprocess.run(full_command, shell=True)

    autogui.hotkey('ctrl', 'f')

    for i in range(1, target_tab):
        autogui.press('tab')
        
    autogui.hotkey('enter')
    speak(blueberry_message)
