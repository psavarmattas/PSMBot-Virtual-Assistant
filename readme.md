# **Create your own virtual assistant with just a few lines code (Using only PYTHON)**

_`Last Updated: December 22' 2020`_

Hello & Welcome to this git page. Here I just created my own 
virtual assistant with just a few lines of code. It is not an 
issue if you are a beginner, or an advanced coder this way of 
building your own virtual assistant is very simple and quick.

The only major thing required from your side is the will to go
step by step with me and by the end of it you will have your own
virtual assistant up & running as a charm.

To learn more about how I did it you can watch my YouTube
video on this or [click here]().

## Pre-Requisites:
1. Python Interpreter (Like [PyCharm](https://www.jetbrains.com/pycharm/))
2. Python Environment (Like [Anaconda](https://www.anaconda.com/products/individual))
3. This [git repo](https://github.com/psavarmattas/PSMBot-Virtual-Assistant.git)
4. Bellow mentioned python packages:

-> [speechrecognition](https://pypi.org/project/SpeechRecognition/)

-> [pyttsx3](https://pypi.org/project/pyttsx3/)

-> [pywhatkit](https://pypi.org/project/pywhatkit/)

-> [wikipedia](https://pypi.org/project/wikipedia/)

-> [pyjokes](https://pypi.org/project/pyjokes/)

5. Basic knowledge of how Python works & computers work
6. A will to explore

When all the above pre-requisites are there and ready you can 
start to work on your own virtual assistant. Please follow each 
and every step in order & if you have any error just go to the issues
to see if you find any issue that matches your which is already 
resolved before opening an issues.

## Steps:

### For Windows users:
1. Open PyCharm & create a new project with your virtual environment ready.
2. Open the terminal and paste the following in sequential order line by line(Execute it one by one):

`pip install speechRecognistion`

`pip install pyttsx3`

`pip install pywhatkit`

`pip install wikipedia`

`pip install pyjokes`

_Install this if necessary (Only when the code gives error)_

`pip install pyaudio`

3. Copy the code given in main.py (in this git) & you will have the code up & running on your pc.
_(Note: Creating two different files for weather & main you will have to import weather.py in the main.py file by using the `import weather` code in the main.py, therefore please make sure that the code for it is there or an error will be produced while running the weather command in the assistant.)_
4. If you want to learn how this code actually works the go [watch my YouTube video]() for a better understanding.

### For Linux/MacOs users:

1. Learn all the above commands on terminal. 
2. Make sure to use pip3, because in linux pip refers for python2 and pip3 refers to python3.
3. Install these too - `pip3 install pyAudio`.


## Feature List (v1.0):

1. Play videos on YouTube.
2. Search wikipedia with your queries.
3. Search google with your queries.
4. Listen to jokes.
5. Ask for the weather (only New Delhi, India available right now).