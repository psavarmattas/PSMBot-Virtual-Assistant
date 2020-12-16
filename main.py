#  Copyright (c) 2020 PSMForums. All rights reserved.
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#  http://www.apache.org/licenses/LICENSE-2.0
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import json
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import weather

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        command = r.recognize_google(audio, language='en-in')
        print(f"User said: {command}\n")

    except Exception as e:

        print("Say that again please...")
        return "None"
    return command


if __name__ == "__main__":

    while True:

        command = take_command().lower()

        if 'play' in command:
            song = command.replace('play', '')
            talk('playing ' + song)
            pywhatkit.playonyt(song)
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time is ' + time)
        elif 'search' in command:
            wiki = command.replace('wiki', '')
            info = wikipedia.summary(wiki, 6)
            print(info)
            talk(info)
        elif 'date' in command:
            talk('sorry, I have a headache')
        elif 'are you single' in command:
            talk('I am in a relationship with PSMForums')
        elif 'joke' in command:
            talk('Let me get you laughing')
            talk(pyjokes.get_joke())
        elif 'weather' in command:
            command = command.replace('weather', '')
            if weather.response.status_code == 200:
                talk('The Weather In:')
                talk(weather.weather_city)
                print(weather.weather_city)
                talk(weather.weather_temperature)
                print(weather.weather_temperature)
                talk(weather.weather_humidity)
                print(weather.weather_humidity)
                talk(weather.weather_pressure)
                print(weather.weather_pressure)
                talk(weather.weather_report)
                print(weather.weather_report)
            else:
                talk(weather.weather_error)
                print(weather.weather_error)
        elif 'stop' in command:
            break
        else:
            talk('Please say the command again.')