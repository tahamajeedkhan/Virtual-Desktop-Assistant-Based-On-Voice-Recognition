import datetime
import speak
import webbrowser
import weather
import os
import calendar
import subprocess
import speech_recognition as sr

def get_calendar_events():
    cal = calendar.Calendar()
    events = cal.monthdays2calendar(datetime.datetime.now().year, datetime.datetime.now().month)
    return events

def open_application(application_name):
    try:
        subprocess.Popen(application_name)
        speak.speak(f"{application_name} is now open")
    except Exception as e:
        speak.speak(f"Unable to open {application_name}: {str(e)}")

def calculate_expression(expression):
    try:
        result = eval(expression)
        speak.speak(f"The result of {expression} is {result}")
        return f"The result of {expression} is {result}"
    except Exception as e:
        speak.speak(f"Unable to calculate the expression: {str(e)}")
        return "Unable to calculate the expression"

def listen_for_expression():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for expression...")
        audio = recognizer.listen(source)
    try:
        print("Recognizing expression...")
        expression = recognizer.recognize_google(audio)
        print(f"User said: {expression}")
        return expression
    except sr.UnknownValueError:
        print("Could not understand audio")
        return None
    except sr.RequestError as e:
        print(f"Error retrieving recognition results from Google Speech Recognition service: {e}")
        return None

def Action(send):
    data_btn = send.lower()

    if "what is your name?" in data_btn:
        speak.speak("my name is virtual Assistant")
        return "my name is virtual Assistant"

    elif "hello" in data_btn or "hi" in data_btn:
        speak.speak("Hey sir, How i can  help you !")
        return "Hey sir, How i can  help you !"

    elif "how are you" in data_btn:
        speak.speak("I am doing great these days sir")
        return "I am doing great these days sir"

    elif "thank you" in data_btn or "thank" in data_btn:
        speak.speak("its my pleasure sir to stay with you")
        return "its my pleasure sir to stay with you"

    elif "good morning" in data_btn:
        speak.speak("Good morning sir, i think you might need some help")
        return "Good morning sir, i think you might need some help"

    elif "time now" in data_btn or "current time" in data_btn:
        current_time = datetime.datetime.now()
        Time = (str)(current_time.hour) + " Hour : ", (str)(current_time.minute) + " Minute"
        speak.speak(Time)
        return str(Time)

    elif "shutdown" in data_btn or "quit" in data_btn:
        speak.speak("ok sir")
        return "ok sir"

    elif "open spotify" in data_btn or "spotify" in data_btn:
        webbrowser.open("https://spotify.com/")
        speak.speak("spotify.com is now ready for you, enjoy your music")
        return "spotify.com is now ready for you, enjoy your music"

    elif 'open google' in data_btn or 'google' in data_btn:
        open_application("chrome")
        return "Opening Google Chrome"

    elif 'open facebook' in data_btn or 'facebook' in data_btn:
        open_application("firefox")
        return "Opening Mozilla Firefox"

    elif 'youtube' in data_btn or "open youtube" in data_btn:
        open_application("firefox https://youtube.com/")
        return "Opening YouTube in Microsoft Edge"

    elif 'play songs' in data_btn or "songs" in data_btn:
        speak.speak("What song do you want to play?")
        song_name = listen_for_expression()
        if song_name:
            webbrowser.open(f"https://www.youtube.com/results?search_query={song_name.replace(' ', '+')}")
            speak.speak(f"Playing {song_name}")
            return f"Playing {song_name}"
        else:
            return "Unable to recognize song name. Please try again."

    elif 'weather' in data_btn:
        ans = weather.Weather()
        speak.speak(ans)
        return ans

    elif 'music from my laptop' in data_btn:
        url = 'D:\\Songs'
        songs = os.listdir(url)
        os.startfile(os.path.join(url, songs[0]))
        speak.speak("songs playing...")
        return "songs playing..."

    elif 'calendar events' in data_btn:
        events = get_calendar_events()
        speak.speak("Here are your upcoming events:")
        for week in events:
            for day, event in week:
                if event:
                    speak.speak(f"{day}: {event}")
        return "Here are your upcoming events"

    elif 'calculate' in data_btn:
        speak.speak("Do you want to enter the expression or speak it?")
        response = listen_for_expression()
        if response:
            return calculate_expression(response)
        else:
            return "Unable to recognize expression. Please try again."

    else:
        speak.speak("I'm unable to understand!")
        return "I'm unable to understand!"

