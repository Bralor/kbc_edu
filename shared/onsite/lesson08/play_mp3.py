import os
import time
import subprocess

countdown = 3

while countdown != 0:
    time.sleep(1)
    print(f"Ještě ne, zbývá {countdown} s ..")
    countdown -= 1

# subprocess.Popen(['/usr/bin/mpg123', '../onsite/lesson08/monster-kill-dota-2-sound.mp3'], shell=True)  # bez shell=True
os.system("mpg123" + ' announcer.mp3')
