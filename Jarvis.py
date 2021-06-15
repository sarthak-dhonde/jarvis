import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import PyInstaller
import os

print("READ THIS")
print("WHAT YOUR JARVIS CAN DO")
print("Your Jarvis can search in chrome\n can summarize wikipedia\n can open google and youtube\n  can show you IPL score\n can open National Geographic\n can recommend the best educational channel \n can open the famous coding YT Channel Code With Harry\n can show you recommended Hindi news channel\n Can plat latest music playlist having more than 1000 songs from T Series\n can show you recommended marathi news channel\n can open Adobe Reader 9\n can open amazon\n can also open recommended coding website of stack overflow\n can also tell present time\n can also open SonyLiv website")
print("Jarvis can also answer your questions as\n How are you?\n Who are you?\n How do you do?\n What are you doing?\n What is your name?\n Are you a robot? ")
print("Your Jarvis can also reply on your comments like\n Really!\n Hello\n I am fine\n")
print("Your Jarvis can quit by saying\n Quit \n Bye \n Goodbye \n Exit \n \n \n")
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

print("Enter your Name:")
username = str(input())


def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good Morning Sir')
    elif hour>=12 and hour<18:
        speak('Good Afternoon sir')
    else:
        speak('Good Evening sir')    

    speak('I am Jarvis. How can I help you?')   
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en')
        print(f"User said: {query}\n")

    except Exception as e:

        print("say that again pls sir")
        return "None"
    return query       


if __name__ == "__main__":
   wishMe()
   while True:
        query = takeCommand().lower()
   #executing task based on query


        if'wikipedia' in query:
            speak('Searching wikipedia')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif'youtube' in query:
            webbrowser.open("www.youtube.com")
        elif'google' in query:
            webbrowser.open("www.google.com")
        elif'how are you' in query:
            speak("I am fine")
            print("I am fine")
        elif'what are you doing' in query:
            speak("I am spending time with you") 
            print("I am spending time with you")
        elif'what is your name' in query:
            speak("My name is Jarvis sir")
            print("My name is Jarvis, sir")
        elif'who are you' in query:
            speak("I am Jarvis sir")
            print("I am Jarvis sir")
        elif'well done' in query:
            speak("Thank you its my pleasure")
            print("Thank you its my pleasure") 
        elif'thank you' in query:
            speak("You are welcome sir")
            print("You are welcome sir")
        elif'ipl updates' in query:
            webbrowser.open("https://www.google.com/search?source=hp&ei=PXyuX8iNLJXfz7sP_oya2AM&q=cricket&oq=cricket&gs_lcp=CgZwc3ktYWIQAzIFCAAQsQMyAggAMggILhCxAxCDATIFCAAQsQMyBQgAELEDMgIIADIFCC4QsQMyBQgAELEDMgUIABCxAzIFCAAQsQM6CAgAELEDEMkDOgIILjoICAAQsQMQgwE6CAguEMcBEKMCOggIABDqAhCPAToOCC4QsQMQxwEQowIQkwI6CggAELEDELEDEApQ_7cLWPjgC2Cy4wtoBnAAeACAAa4BiAGfC5IBBDEuMTKYAQCgAQGqAQdnd3Mtd2l6sAEK&sclient=psy-ab&ved=0ahUKEwiIoJP6wv_sAhWV73MBHX6GBjsQ4dUDCAc&uact=5")
            speak("This is the official website for Indian Premiere League")
        elif'exit' in query:
            speak(f"Goodbye {username}, Take care")
            print(f"Goodbye {username}, Take care")
            exit()
        elif'bye' in query:
            speak("Bye sir see you next time")
            exit()
        elif'goodbye' in query:
            speak("Goodbye sir, see you next time")
            exit()
        elif'play music'in query:
            webbrowser.open("https://www.youtube.com/aashiqui2/videos")
            speak("These are the music from T-Series YouTube Channel")
        elif'really' in query:
            speak("yeah sir")
        elif'are you robot' in query:
            speak("yes sir, I am Jarvis, a desktop assistant.")
            print("yes sir, I am Jarvis, a desktop assistant.")
        elif'scientific hindi' in query:
            webbrowser.open("https://www.youtube.com/c/FactTechz/videos")
            speak("This is the most famous science fiction YouTube channel in hindi named Facttechz")
        elif'hindi science' in query:
            webbrowser.open("https://www.youtube.com/c/FactTechz/videos")
        elif'hindi scientific' in query:
            webbrowser.open("https://www.youtube.com/c/FactTechz/videos")
            speak("This is the most famous science fiction YouTube channel in hindi named Facttechz")
        elif'play latest music' in query:
            webbrowser.open("https://www.youtube.com/watch?v=b8--JS9lRnI&list=PL095CA373D64B70C0")
            speak("This is the playlist of latest song by T series")
        elif'hello' in query:
            speak(f"hello {username}")
            print(f"hello {username}")
        elif'quit' in query:
            speak("Bye")
            print("Bye")
            exit()
        elif'scientific channel' in query:
            webbrowser.open("https://www.youtube.com/c/NatGeo/videos")
            speak("This is the best scientific YouTube channel names National Geographic")
        elif'codewithharry' in query:
            webbrowser.open("https://www.youtube.com/c/CodeWithHarry/videos")
            speak("This is the best coding YouTube channel named Code With Harry")
        elif'best educational channel' in query:
            webbrowser.open("https://www.youtube.com/c/DearSir/videos")
            speak("This is the most best educational youtube channel, who teaches English and Mathematics for seondary, high secondary and students who are preparing themselves for competitive exams and also teaches us English speaking and short tricks for Maths. This channel is named as Dear Sir")
        elif'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is{strTime}")
        elif'stack overflow' in query:
            webbrowser.open("www.stackoverflow.com")
            speak("This is one of the recommended website named stack overflow which teaches you coding")
        elif'how do you do' in query:
            speak("I am fine sir, what about you")
            print("I am fine sir, what about you?")
        elif'am fine' in query:
            speak("Nice to hear that from you sir")
            print("Nice to hear that from you sir")
        elif'show news in hindi' in query:
            webbrowser.open("https://www.youtube.com/watch?v=SmQqAnKG6zs")
            speak("This is the live news from hindi")
        elif'live news' in query:
            webbrowser.open("https://www.youtube.com/watch?v=9Auq9mYxFEE")
            speak("This is the live news from Sky News in English")
        elif'marathi news' in query:
            webbrowser.open("https://www.youtube.com/watch?v=itJLgnqZ3U8")
            speak("This is the live news from ABP maza in marathi")    
        elif'news in marathi' in query:
            webbrowser.open("https://www.youtube.com/watch?v=itJLgnqZ3U8")
            speak("This is the live news from ABP maza in marathi")    
        elif'amazon' in query:
            webbrowser.open("https://www.amazon.in/?ext_vrnc=hi&tag=googhydrabk-21&ascsubtag=_k_EAIaIQobChMIipy3m8iB7QIVBpZLBR3Lqwg6EAAYASAAEgJNlfD_BwE_k_&ext_vrnc=hi&gclid=EAIaIQobChMIipy3m8iB7QIVBpZLBR3Lqwg6EAAYASAAEgJNlfD_BwE")
            speak("This the shopping website named amazon")
        elif'shopping' in query:
            webbrowser.open("https://www.amazon.in/?ext_vrnc=hi&tag=googhydrabk-21&ascsubtag=_k_EAIaIQobChMIipy3m8iB7QIVBpZLBR3Lqwg6EAAYASAAEgJNlfD_BwE_k_&ext_vrnc=hi&gclid=EAIaIQobChMIipy3m8iB7QIVBpZLBR3Lqwg6EAAYASAAEgJNlfD_BwE")
            speak("This the shopping website named amazon")
        elif'sonyliv' in query:
            webbrowser.open("https://www.sonyliv.com/")
            speak("This is the sony leave website. You can use it for watching TV shows")
        elif'best entertaining' in query: 
            webbrowser.open("https://www.sonyliv.com/")
            speak("This is the sony leave website. You can use it for watching TV shows")
        elif'adobe reader' in query: 
            adobePath = "C:\Program Files (x86)\Adobe\Reader 9.0\Reader\AcroRd32.exe"
            os.startfile(adobePath)
            speak("starting adobe reader 9")
        elif'search' in query:
            speak("what should I search sir")
            search = takeCommand()
            chrompath = "C://Program Files//Google//Chrome//Application//chrome.exe %s"
            speak("Ok sir")
            webbrowser.get(chrompath).open_new_tab(search+'.com')
            exit()
        elif'national geographic'in query:
            webbrowser.open("https://www.youtube.com/c/NatGeo/videos")
            speak("This is the best scientific YouTube channel names National Geographic")
        elif'hindi news' in query:
            webbrowser.open("https://www.youtube.com/watch?v=SmQqAnKG6zs")
            speak("This is the live news from hindi")   
        elif'yokibu' in query:
            webbrowser.open("https://www.yokibu.com/home")
            speak("Starting yokibu")   
        elif'open gmail' in query:
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
            speak("Starting Google Mail")   
        elif'meet' in query:
            webbrowser.open("https://meet.google.com/")
            speak("Starting Google Meet") 

