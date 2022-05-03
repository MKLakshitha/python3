import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = sr.Recognizer()

engine = pyttsx3.init()

voices = engine.getProperty('voices')

engine.setProperty('voice',voices[5].id)

engine.say('Kavindu, Alexa Speaking..')

engine.say('What can I do for you')

engine.runAndWait()

def talk(text):

    engine.say(text)

    engine.runAndWait()

def take_command():
    
        try:
            with sr.Microphone() as source:
                print('Kavindu, I am listening....')
                listener.adjust_for_ambient_noise(source,duration=0.1)
                voice = listener.listen(source)
                command = listener.recognize_google(voice)
                command = command.lower()
                print(f"Recognized{command}")
                if 'alexa' in command:
                    command = command.replace('alexa', '')
                    talk(command)
                    print(command)
                elif 'time' in command:
                    time = datetime.datetime.now().strftime('%I : %M %p')
                    talk('Current time: ' % time)
                    print(time)
                elif 'Who is ' in command:
                    person = command.replace('Who is ', '')
                    info = wikipedia.summary(person,1)
                    print(info)
                    talk(info)
                elif 'date' in command:
                    talk('Sorry, I have headache today')
                elif 'I Love you' in command:
                    talk('Sorry Bro I already commited with WIFI')
                elif 'Sorry' in command:
                    talk('So Do you say you did not love me')
                elif 'yes' in command:
                    talk('Okay then bye')
                    exit()

        except sr.UnknownValueError:
            talk('Kavindu, I cannot understand')
        
        

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('Playing' + song)
        print('Playing....'+song)
        pywhatkit.playonyt(song)

run_alexa()