import pyaudio
import struct
import pyautogui as autogui
import pvporcupine

def hotword():
    porcupine = None
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
                print("H key pressed")
    except:
        if porcupine is not None:
            porcupine.delete()
        if audio_stream is not None:
            audio_stream.close()
        if paud is not None:
            paud.terminate()

hotword()