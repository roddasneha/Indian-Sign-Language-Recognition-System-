from easygui import buttonbox
import speech_recognition as sr
import socket
from googletrans import Translator
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from itertools import count
import matplotlib.pyplot as plt
import numpy as np
import string

translator = Translator()

gif_lst = ['all the best', 'are you sick', 'any questions', 'are you angry', 'are you busy', 'are you hungry',
           'be careful', 'can we meet tomorrow', 'clean the room', 'did you eat lunch', 'did you finish homework',
           'do you go to office', 'do you have money', 'do you want something to drink', 'do you watch tv',
           'dont worry', 'flower is beautiful', 'good afternoon', 'good morning', 'good question', 'good evening',
           'good night', 'happy journey', 'what do you want tea or coffee', 'what is your name',
           'how many people are in your family', 'i am a clerk', 'i am bored', 'i am fine', 'i am sorry',
           'i am thinking', 'i am tired', 'i dont understand anything', 'i go to a theatre', 'i love to shop',
           'i had to say something but i forgot', 'i have a headache', 'i like pink colour', 'lets go for lunch',
           'my mother is a housewife', 'nice to meet you', 'please dont smoke', 'open the door', 'call me later',
           'please call the ambulance', 'give me your pen', 'please wait for sometime', 'can i help you',
           'shall we go together tomorrow', 'sign language interpreter', 'sit down', 'stand up', 'take care',
           'there was a traffic jam', 'wait I am thinking', 'what are you doing', 'what is the problem',
           'what is todays date', 'what does your father do', 'what is your job', 'what is your age',
           'what is your mobile number', 'what is your name', 'whats up', 'when is your interview',
           'when will we go', 'where do you live', 'where is the bathroom', 'where is the police station',
           'you are wrong']

lst = list(string.ascii_lowercase)

def is_connected():
    try:
        host = socket.gethostbyname("one.one.one.one")
        s = socket.create_connection((host, 80), 2)
        s.close()
        return True
    except:
        return False

def animate(aud1, aud):
    if aud1 in gif_lst:
        class ImageLabel(tk.Label):
            def load(self, img):
                if isinstance(img, str):
                    img = Image.open(img)
                self.loc = 0
                self.frames = []
                try:
                    for i in count(1):
                        self.frames.append(ImageTk.PhotoImage(img.copy()))
                        img.seek(i)
                except EOFError:
                    pass
                try:
                    self.delay = img.info['duration']
                except:
                    self.delay = 100
                if len(self.frames) == 1:
                    self.config(image=self.frames[0])
                else:
                    self.next_frame()

            def unload(self):
                self.config(image=None)
                self.frames = None

            def next_frame(self):
                if self.frames:
                    self.loc += 1
                    self.loc %= len(self.frames)
                    self.config(image=self.frames[self.loc])
                    self.after(self.delay, self.next_frame)

        root = tk.Tk()
        lbl = ImageLabel(root)
        lbl.pack()
        lbl.load(f'Indian_Speech_Language_GIFS/{aud1}.gif')
        text = Text(root, height=5)
        text.insert(INSERT, aud)
        text.pack()
        Button(root, text="Quit", command=root.destroy).pack()
        root.mainloop()
    else:
        for char in aud1:
            if char in lst:
                img_path = f'Alphabets/{char}.jpg'
                img = Image.open(img_path)
                plt.imshow(np.asarray(img))
                plt.text(530, -40, aud, fontsize=12)
                plt.pause(0.8)
        plt.close()

def translate_text(text):
    return translator.translate(text, src="hi", dest="en").text

def takeCommandHindi():
    aud = ""
    if is_connected():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening")
            r.pause_threshold = 0.7
            audio = r.listen(source)
            try:
                print("Recognizing")
                query = r.recognize_google(audio, language="hi-In")
                aud = translate_text(query)
                print(aud)
            except Exception as e:
                print(e)
                print("Oops! Say That Again...")
                return
    else:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening")
            r.pause_threshold = 0.7
            audio = r.listen(source)
            try:
                print("Recognizing")
                aud = r.recognize_sphinx(audio)
                print(aud)
            except sr.UnknownValueError:
                print("Oops! Say That Again...")
            except sr.RequestError as e:
                print(f"Sphinx error; {e}")

    aud1 = aud.lower()
    aud1 = aud1.translate(str.maketrans('', '', string.punctuation))
    animate(aud1, aud)

i = 0
while True:
    ch = ["Speak Again" if i > 0 else "Speak", "Exit"]
    box = buttonbox("IT'S NOT JUST ABOUT THE HANDS", image="SignLanguage.png", choices=ch)
    i += 1
    if box == ch[0]:
        takeCommandHindi()
    else:
        quit()
