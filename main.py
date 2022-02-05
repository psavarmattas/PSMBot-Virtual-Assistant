#  Copyright (c) 2021 PSMForums. All rights reserved.
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
import wolframalpha
import weather
import requests, json
import pprint

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)

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
            talk('playing ' + song + 'opening web browser')
            pywhatkit.playonyt(song)
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time is ' + time)
        elif 'search on google' in command:
            searchg = command.replace('search on google', '')
            pywhatkit.search(searchg)
            talk('Searching' + searchg + 'opening web browser')
        elif 'date' in command:
            talk('sorry, I have a headache')
        elif 'are you single' in command:
            talk('I am in a relationship with PSMForums')
        elif 'joke' in command:
            talk('Let me get you laughing...')
            talk(pyjokes.get_joke())
        elif "what is the weather in" in command:
            command = command.split(" ")
            location = str(command[5])
            url = weather.weather_url + "appid=" + weather.api_key + "&q=" + location 
            js = requests.get(url).json() 
            if js["cod"] != "404": 
                weather = js["main"] 
                temp = weather["temp"] 
                hum = weather["humidity"] 
                desc = js["weather"][0]["description"]
                resp_string = "The temperature at " + location + " in Kelvin is " + str(temp) + " \nThe humidity is " + str(hum) + "\nand \nThe weather description is "+ str(desc)
                print(resp_string)
                talk(resp_string)
            else:
                print("City Not Found") 
                talk("City Not Found")
        elif 'calculate' in command:
            app_id = "JWP25T-Y434EXL697" #Your API key here
            client = wolframalpha.Client(app_id) 
            indx = command.lower().split().index('calculate') 
            query = command.split()[indx + 1:] 
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print('The answer is ' + answer)
            talk('The answer is:' + answer)
        elif 'thank you' in command:
            talk('Your welcome, Happy to help you')
        elif 'thanks' in command:
            talk('Your welcome, Happy to help you')
        elif 'stop' in command:
            break
        else:
            talk('Please say the command again.')