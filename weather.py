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

# importing requests and json
import requests, json

# base URL
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

# City Name
CITY = "New Delhi"

# API key
API_KEY = "a4212b9586f6bf848e1c47839ebfc5e9"

# Updating the URL
URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY

# HTTP request
response = requests.get(URL)

# checking the status code of the request

if response.status_code == 200:

    # getting data in the json format
    data = response.json()

    # getting the main dict block
    main = data['main']

    # getting temperature
    temperature = main['temp']

    # getting the humidity
    humidity = main['humidity']

    # getting the pressure
    pressure = main['pressure']

    # weather report

    report = data['weather']
    weather_city = f"{CITY:-^30}"
    weather_temperature = f"Temperature: {temperature}"
    weather_humidity = f"Humidity: {humidity}"
    weather_pressure = f"Pressure: {pressure}"
    weather_report = f"Weather Report: {report[0]['description']}"

else:
    # showing the error message
    weather_error = "Error in the HTTP request please try again"
