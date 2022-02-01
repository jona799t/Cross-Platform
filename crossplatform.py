import sys
import os
if os.name == 'nt':
    import msvcrt
    import winsound
else:
    from pynput.keyboard import Listener
    from playsound import playsound

def clear():
    os.system('cls' if os.name in ('nt', 'dos') else 'clear')

def title(whatToTitle):
    os.system("title " + whatToTitle) if os.name in ('nt', 'dos') else sys.stdout.write(f"\x1b]2;{whatToTitle}\x07")

def play(fileLocation):
    if os.name == 'nt':
        winsound.PlaySound(fileLocation, winsound.SND_FILENAME)
    else:
        playsound(fileLocation)

def waitForKey(keyToWaitFor):
    if os.name == 'nt':
        while True:
            if msvcrt.kbhit():
                key = str(msvcrt.getch(), encoding="utf-8")
                if key.lower() == keyToWaitFor:
                    return True
    else:
        def on_press(key):
            if str(key).replace("\'", "").lower() == keyToWaitFor:
                return False
        with Listener(
            on_press=on_press,
            on_release=None) as listener:
            listener.join()
        return True
