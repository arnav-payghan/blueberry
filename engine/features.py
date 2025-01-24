from playsound import playsound
import eel


@eel.expose
def playAssistantSound():   # Start PopUp Sound for Assistant
    music_dir = "frontend\\assets\\audio\\popup_sound.mp3"
    playsound(music_dir)