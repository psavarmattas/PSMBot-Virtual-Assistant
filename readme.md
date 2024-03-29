# **Create your own virtual assistant with just a few lines code (Using only PYTHON)**

_`Last Updated: February 05' 2022`_

Hello & Welcome to this git page. Here I just created my own 
virtual assistant with just a few lines of code. It is not an 
issue if you are a beginner, or an advanced coder this way of 
building your own virtual assistant is very simple and quick.

The only major thing required from your side is the will to go
step by step with me and by the end of it you will have your own
virtual assistant up & running as a charm.

To learn more about how I did it you can watch my YouTube
video on this or [click here](https://www.youtube.com/channel/UCz6SDxk2KQqJAD6Ra_YPm6A).

## Pre-Requisites:

1. Python Interpreter (Like [PyCharm](https://www.jetbrains.com/pycharm/))
2. Python Environment (Like [Anaconda](https://www.anaconda.com/products/individual))
3. This [git repo](https://github.com/psavarmattas/PSMBot-Virtual-Assistant.git)
4. Bellow mentioned python packages:

-> [speechrecognition](https://pypi.org/project/SpeechRecognition/)

-> [pyttsx3](https://pypi.org/project/pyttsx3/)

-> [pywhatkit](https://pypi.org/project/pywhatkit/)

-> [pyjokes](https://pypi.org/project/pyjokes/)

-> [wolframalpha](https://pypi.org/project/wolframalpha/)

5. Basic knowledge of how Python works & computers work
6. A will to explore
7. Get API keys for the following to test your assistant yourself or 
just use the one I provide you with but it is better to use your API keys 
so that you don't bottle neck you assistant.

When all the above pre-requisites are there and ready you can 
start to work on your own virtual assistant. Please follow each 
and every step in order & if you have any error just go to the issues
to see if you find any issue that matches your which is already 
resolved before opening an issues.

## Steps:

### For Windows users:

1. Open PyCharm & create a new project with your virtual environment ready.
2. Open the terminal and paste the command highlighted below:

`pip install -r requirements.txt `

_Install this if necessary (Only when the code gives error)_

`pip install pyaudio`

3. Copy the code given in main.py (in this git) & you will have the code up & running on your pc.
_(Note: Creating two different files for weather & main you will have to import weather.py in the main.py file by using the `import weather` code in the main.py, therefore please make sure that the code for it is there or an error will be produced while running the weather command in the assistant.)_
4. If you want to learn how this code actually works the go [watch my YouTube video](https://www.youtube.com/channel/UCz6SDxk2KQqJAD6Ra_YPm6A) for a better understanding.

### For Linux/MacOs users:

1. Learn all the above commands on terminal. 
2. Make sure to use pip3, because in linux pip refers for python2 and pip3 refers to python3.
3. Install this too - `pip3 install pyAudio`.


## Feature List (v2.0):

1. Play videos on YouTube.
2. Search google with your queries.
3. Listen to jokes.
4. Ask for the weather (Anywhere in the world).
5. It can solve complex math problems for you.
6. Ask it for today's date & time.
7. Say "thanks" or "thank you" and the assistant will appreciate you.
8. One command requirements install.