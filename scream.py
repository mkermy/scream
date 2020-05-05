import os
import time

import random
import urllib.request

from playsound import playsound
from tkinter import *

# Check Files

try:
    os.mkdir('audio')
except FileExistsError:
    pass

# Downloading Files

def download():
    files = os.listdir()

    downloadName = ['audio/startAudio.mp3','audio/goodbye.mp3']

    combo = {
    'audio/startAudio.mp3':'https://glados.c-net.org/files/GLaDOS-29941.wav',
    'audio/goodbye.mp3':'http://cdn.frustra.org/sounds/sound_portal1/npc/turret_floor/turret_retire_5.mp3?id=344'
    }

    if not downloadName in files:
        for i,x in combo.items():
            print(i)
            print(x)
            urllib.request.urlretrieve(x,i)
            playsound(i)
    else:
        pass

def generateTime():
    max_number = 60

    first_number = random.randint(20,30)
    second_number = random.randint(10,20)

    while True:
        if first_number+second_number == max_number:
            print(str(first_number) + " " + str(second_number))
            print("Done")
            break
        else:
            sum = first_number + second_number
            ammount_left = max_number - sum
            ammount_left = ammount_left // 2

            print(f"sum: {sum}")
            print(f"ammount left: {ammount_left}")

            second_number = second_number + ammount_left
            first_number = first_number + ammount_left + 1
            print(str(first_number) + " " + str(second_number))
            continue
    return [first_number, second_number]

def main():
    numbers = generateTime()

    download()

    files = os.listdir()

    combo={
    'audio/advanced_cunt.mp3':"http://cache-a.oddcast.com/tts/gen.php?EID=3&LID=1&VID=3&TXT=what%20a%20stupid%20cunt.%20fuck%20you.fuck%20you.fuck%20you.fuck%20you.fuck%20you.fuck%20you.fuck%20you.fuck%20you.fuck%20you.fuck%20you.fuck%20you.fuck%20you.fuck%20you.fuck%20you.fuck%20you.fuck%20you.fuck%20you.fuck%20you.fuck%20you.fuck%20you.%20bitch.&IS_UTF8=1&EXT=mp3&FNAME=&ACC=5883747&API=&SESSION=&CS=e1f4c6faca5d6a6cc2f4a16a02ba7864&cache_flag=3",
    'audio/cunt.mp3':"http://cache-a.oddcast.com/tts/gen.php?EID=3&LID=1&VID=3&TXT=what%20a%20stupid%20cunt&IS_UTF8=1&EXT=mp3&FNAME=&ACC=5883747&API=&SESSION=&CS=50f9f344a9fb3a6195bc666b64eceaed&cache_flag=3",
    'audio/dumbass.mp3':"http://cache-a.oddcast.com/tts/gen.php?EID=3&LID=1&VID=3&TXT=you%20have%20done%20nothing%20with%20your%20life%20do%20you%20really%20think%20that%20your%20work%20has%20effected%20anyone&IS_UTF8=1&EXT=mp3&FNAME=&ACC=5883747&API=&SESSION=&CS=5c3accd09ef49c86c4c91e814e6440a7&cache_flag=3",
    'audio/dumbcunt.mp3':"http://cache-a.oddcast.com/tts/gen.php?EID=3&LID=1&VID=3&TXT=fuck%20you.%20you%20dumb%20cunt.&IS_UTF8=1&EXT=mp3&FNAME=&ACC=5883747&API=&SESSION=&CS=34428e303a5aa0f0dd04c4861dbdcaad&cache_flag=3",
    'audio/life.mp3':"http://cache-a.oddcast.com/tts/gen.php?EID=3&LID=1&VID=3&TXT=does%20life%20matter%20that%20much.%20whats%20the%20point%20of%20life.%20man%20you%20are%20fucking%20retarded&IS_UTF8=1&EXT=mp3&FNAME=&ACC=5883747&API=&SESSION=&CS=251748ee675452c563680f3aaea8f9e3&cache_flag=3",
    'audio/pickle.mp3':"http://cache-a.oddcast.com/tts/gen.php?EID=3&LID=1&VID=3&TXT=he%20turned%20himself%20into%20a%20pickle...%20funniest%20shit%20i%20have%20ever%20seen&IS_UTF8=1&EXT=mp3&FNAME=&ACC=5883747&API=&SESSION=&CS=34af653d48de3d865753028b45444b10&cache_flag=3",
    'audio/hell.mp3':"http://cache-a.oddcast.com/tts/gen.php?EID=3&LID=1&VID=3&TXT=alright%20so%20i%20just%20reserved%20a%20place%20for%20you%20in%20hell.%20where%20you%20belong&IS_UTF8=1&EXT=mp3&FNAME=&ACC=5883747&API=&SESSION=&CS=956f2fba77e1c833f99552c640fafc48&cache_flag=3"}

    for d in combo:
        if d in files:
            pass
        else:
            for i,x in combo.items():
                print(i)
                print(x)
                urllib.request.urlretrieve(x,i)
                time.sleep(random.choice(numbers))
                playsound(i)


def startProgram(fileName="startAudio.mp3"):
    main()

def ending(fileName="goodbye.mp3"):
    global root

    playsound(fileName)
    root.quit()

#download = urllib.urlopen('http://cdn.frustra.org/sounds/sound/vo/glados/epilogue19.mp3?id=621')

## Graphics

root = Tk()
root.title("Scream")
root.geometry("1280x720")

# Buttons

startButton = Button(root,text="Start",command=startProgram,width=25,height=25)
endButton = Button(root,text="End",command=ending,width=25,height=25)

# Placement

startButton.pack(side="left")
endButton.pack(side="right")

# Loop/Start Program
root.mainloop()
