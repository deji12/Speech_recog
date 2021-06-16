import speech_recognition as sr 

from playsound import playsound

import os

def new_folder():

    playsound(r'C:\Users\Ayodeji\Desktop\speec_recog\help.mp3')

    hi_there = 'How may i help you today?'

    print('>>> Listening')

    r = sr.Recognizer()

    mic = sr.Microphone()

    with mic as source:
        r.adjust_for_ambient_noise(source)

        audio = r.listen(source)

    help_ = r.recognize_google(audio)

    if help_ == 'new folder' or help_ == 'New Folder' or help_ == 'NEW FOLDER':

        playsound(r'C:\Users\Ayodeji\Desktop\speec_recog\folder.mp3')

        print('>>> Listening')

        r = sr.Recognizer()

        mic = sr.Microphone()

        with mic as source:

            r.adjust_for_ambient_noise(source)

            audio = r.listen(source)

        new_folder = r.recognize_google(audio)

        print(new_folder)

        os.chdir(r'C:\Users\Ayodeji\Desktop')

        os.mkdir(new_folder)

new_folder()