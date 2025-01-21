import os
import eel
from engine.features import *

eel.init('frontend')

playAssistantSound()

os.system('start msedge.exe --app="http://localhost:8080/index.html"')

eel.start('index.html', port=8080, mode=None, host='localhost', block=True)