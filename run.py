import multiprocessing

# USED TO START BLUEBERRY
def startBlueberry():
    print("Blueberry is running.")
    from main import start
    start()

# LISTENS FOR HOTWORD
def listenHotword():
    print("Listening for Hotword...")
    from engine.features import hotword
    hotword()

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=startBlueberry)
    p2 = multiprocessing.Process(target=listenHotword)
    p1.start()
    p2.start()
    p1.join()

    if p2.is_alive():
        p2.terminate()
        p2.join()
    print("Blueberry has stopped.")