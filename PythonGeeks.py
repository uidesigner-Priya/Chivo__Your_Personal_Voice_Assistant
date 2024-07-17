# ==== Importing all the necessary libraries
import speech_recognition as sr
from ecapture import ecapture as ec
import os
import wikipedia
import pyjokes
import pyttsx3
import webbrowser
import datetime
from tkinter import *
from PIL import ImageTk


# ==== Class Assistant
class assistance_gui:
    def __init__(self,root):
        self.root = root
        self.root.title("Voice Assistant")
        self.root.geometry('600x600')

        self.bg = ImageTk.PhotoImage(file="images/background.png")
        bg = Label(self.root, image=self.bg).place(x=0, y=0)
        
        # Set the background image
        bg_label = Label(self.root, image=self.bg)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        # Frame to hold the buttons
        button_frame = Frame(self.root)
        button_frame.place(relx=0.5, rely=0.9, anchor=CENTER)

        # ==== Start button
        start = Button(button_frame, text='START', font=("lexend", 14), command=self.start_option)
        start.pack(side=LEFT, padx=50)

        # ==== Close button
        close = Button(button_frame, text='CLOSE', font=("lexend", 14), command=self.close_window)
        close.pack(side=RIGHT, padx=50)

    # ==== start assitant
    def start_option(self):
        listener = sr.Recognizer()
        engine = pyttsx3.init()

        # ==== Voice Control
        def speak(text):
            engine.say(text)
            print(text)
            engine.runAndWait()

        # ====Default Start
        def start():
            # ==== Wish Start
            print("Getting started......")
            hour = int(datetime.datetime.now().hour)
            if hour >= 0 and hour < 12:
                wish = "Good Morning!"
            elif hour >= 12 and hour < 18:
                wish = "Good Afternoon!"
            else:
                wish = "Good Evening!"
            speak('Hello mam,' + wish +' I am your voice assistant Chivo. Please tell me how may I help you')
            # ==== Wish End

        # ==== Take Command
        def take_command():
            try:
                with sr.Microphone() as data_taker:
                    print("Say Something")
                    voice = listener.listen(data_taker)
                    instruction = listener.recognize_google(voice)
                    instruction = instruction.lower()
                    return instruction
            except:
                pass

        # ==== Run command
        def run_command():
            instruction = take_command()
            print(instruction)
            try:
                if 'who are you' in instruction:
                    speak('I am your personal voice Assistant Chivo')

                elif 'what can you do for me' in instruction:
                    speak('I can play songs, tell time, and help you go with wikipedia')

                elif 'what is the current time' in instruction:
                    time = datetime.datetime.now().strftime('%I:%M')
                    speak('Yes mam. current time is ' + time)

                elif 'nobel can you open google' in instruction:
                    speak('Yes Opening Google')
                    webbrowser.open('google.com')

                elif 'nobel can you open youtube' in instruction:
                    speak('Yes Opening Youtube')
                    webbrowser.open('youtube.com')
                 
                elif 'play a song' in instruction:
                    speak('Yes playing butter song')
                    webbrowser.open('https://www.youtube.com/watch?v=WMweEpGlu_U')
                    
                elif 'nobel can you play fight scene from naruto' in instruction:
                    speak('Yes playing kakashi fight with zabuza')
                    webbrowser.open('https://www.youtube.com/watch?v=uKtLZzEtoNw')
                    
                elif 'can you search about' in query :
                    query = query.replace("can you search about","")
                    webbrowser.open(query)
                    
                elif 'nobel open opera' in instruction:
                    speak('Yes mam opening opera browser')
                    codePath = r"C:\Users\user\Desktop\Opera Browser.lnk"
                    os.startfile(codePath)
                    
                elif 'can you search about' in instruction:
                    instruction = instruction.replace("nobel can you search about", "")
                    speak('yes mam Searching Wikipedia...')
                    results = wikipedia.summary(instruction, sentences = 3)
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)
                    
                elif 'nobel can you tell me a joke' in instruction:
                    speak('Yes mam...')
                    speak(pyjokes.get_joke())
                    
                elif 'nobel open translator' in instruction:
                    speak('Yes mam opening translator')
                    codePath = r"C:\Users\user\Desktop\Translator.lnk"
                    os.startfile(codePath)

                elif 'nobel open my whatsapp' in instruction:
                    speak('Yes mam opening your whatsapp')
                    codePath = r"C:\Users\user\Desktop\WhatsApp Desktop.lnk"
                    os.startfile(codePath)
                    
                elif 'nobel open my spotify' in instruction:
                    speak('Yes mam opening your spotify')
                    codePath = r"C:\Users\user\Desktop\Spotify.lnk"
                    os.startfile(codePath)

                elif 'nobel can you open wikipedia' in instruction:
                    speak('Opening wikipedia')
                    webbrowser.open('Wikipedia.com')

                elif 'nobel can you open gmail' in instruction:
                    speak('Yes Opening Gmail')
                    webbrowser.open('gmail.com')

                elif 'nobel can you open stack overflow' in instruction:
                    speak('Yes Opening Stack Overflow')
                    webbrowser.open('stackoverflow.com')
                    
                elif "take a photo" in instruction:
                    speak("Yes mam . now say cheese!!!")
                    ec.capture(0, "my camera", "img.jpg")
                    
                elif 'exit' in instruction:
                    speak("Thanks for giving me your time")
                    exit(0)
                    
                elif 'can you shutdown my laptop' in instruction:
                    speak('I am shutting down your laptop')
                    self.close_window()
                    return False
                else:
                    speak('I did not understand, can you repeat again')
            except:
                speak('Waiting for your response')
            return True

        # ====Default Start calling
        start()

        # ====To run assistance continuously
        while True:
            if run_command():
                run_command()
            else:
                break


    # ==== Close window
    def close_window(self):
        self.root.destroy()

# ==== create tkinter window
root = Tk()

# === creating object for class
obj=assistance_gui(root)

# ==== start the gui
root.mainloop()
