import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

mail_contacts = {'admin': 'abcdef@yahoo.com', 'dad': 'xyze@gmail.com'}

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 175)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour >=12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good evening")

    speak("Welcome Doctor Groot. I am System060899."
          " Please tell me how may i help you.")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        audio = r.listen(source)

    try:
        print("Recognzing...")
        query = r.recognize_google(audio, language= 'en-in')
        print(f"User Said: {query}\n")

    except Exception as e:
        print(e)
        # printing exception above

        print("Say it again please....")
        return "None"

    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    # Mail and password to be enter now
    server.login('mail@gmail.com', 'pass')
    server.sendmail('mail@gmail.com', to, content)
    server.close()


def main():
    wishme()
    while True:
        query = takecommand().lower()
        if 'wikipedia' in query:
            speak("Searching..")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(result)
            speak(result)

        elif 'hello system' in query:
            wishme()

        elif 'open youtube' in query:
            speak("YouTube")
            webbrowser.get('C:/Program Files/Google/Chrome/Application/chrome.exe %s').open('https://youtube.com')

        elif 'open google' in query:
            speak("Google")
            webbrowser.get('C:/Program Files/Google/Chrome/Application/chrome.exe %s').open('https://google.com')


        elif 'open github' in query:
            speak("Git Hub")
            webbrowser.get('C:/Program Files/Google/Chrome/Application/chrome.exe %s').open('https://github.com')

        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strtime}")

        elif 'play music' in query:
            os.system('start C:/Users/amanp/Music/faded.mp3')

        elif 'open python' in query:
            os.startfile('C:/Program Files/Python38/python.exe')
            speak("python")

        elif 'open pycharm' in query:
            os.startfile('C:/Program Files/JetBrains/PyCharm Edu 2021.3.2/bin/pycharm64.exe')
            speak("Pycharm")

        elif 'mail to admin' in query:
            a = query.split()
            if a[-1] in mail_contacts:
                speak("What should i say ?")
                content = takecommand()
                print(content)
                to = mail_contacts[a[-1]]
                sendEmail(to, content)
                speak('Email has been sent!')
            else:
                speak("Person not found in Email Contact")
                speak('Please tell the email address')
                mail = takecommand()
                print(mail)
                speak("What should i say ?")
                content = takecommand()
                print(content)
                sendEmail(mail, content)
                speak('Email has been sent!')

        elif 'thanks system' in query:
            msg = 'Happy to help you, Have a nice day'
            speak(msg)
            break

if __name__ == '__main__':
    main()
