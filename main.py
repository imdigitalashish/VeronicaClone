from copyreg import constructor
import json
import eel
import ctypes
user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(78), user32.GetSystemMetrics(79)
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import requests
bot = ChatBot(
    'Norman',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
   
    database_uri='sqlite:///database.sqlite3'
)

trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english")

# print(screensize)


eel.init("web")


def returnBotResponse(text):
    return bot.get_response(text).text


@eel.expose
def returnResponse(input):
    return returnBotResponse(input)

@eel.expose
def wolframeAlphaResponse(input):
    request = requests.get("https://api.wolframalpha.com/v1/result?appid=G3PE54-VKYR55XQ2J&i="+input)
    return request.text

@eel.expose
def getCovid19Summary(input):
    request = requests.get("https://api.covid19api.com/summary")
    response = json.loads(request)
    return response["Global"]

eel.start("index.html", size=screensize)