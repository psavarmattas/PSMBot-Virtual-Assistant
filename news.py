import pyttsx3
import requests 
import json 
import time 

url = ('https://newsapi.org/v2/top-headlines?'
        'country = in&'
        'apiKey =') 

url += 'e3adedf2b3c54560b27338ef2bac6af8' #Your API key here

engine = pyttsx3.init()

voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)

rate = engine.getProperty('rate')

engine.setProperty('rate', 150)

try: 
    response = requests.get(url) 
except: 
    engine.talk("can't access link, please check your internet ") 

news = json.loads(response.text) 

for new in news['articles']:
    # print(str(new['title']), "\n\n") 
    news_title = (str(new['title']))

    # print(str(new['description']), "\n\n") 
    news_description = (str(new['description'])) 
    time.sleep(2) 

# from urllib.request import urlopen
# from bs4 import BeautifulSoup as soup


# def news():
#     try:
#         news_url = "https://news.google.com/news/rss"
#         Client = urlopen(news_url)
#         xml_page = Client.read()
#         Client.close()
#         soup_page = soup(xml_page, "xml")
#         news_list = soup_page.findAll("item")
#         li = []
#         for news in news_list[:15]:
#             li.append(str(news.title.text.encode('utf-8'))[1:])
#         return li
#     except Exception as e:
#         print(e)
#         return False