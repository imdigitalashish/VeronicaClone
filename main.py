import string
import webbrowser
from fastapi import FastAPI
import psutil
app = FastAPI()


@app.get("/cpu")
async def returnCpuTem():
    t = psutil.cpu_times_percent
    return t


@app.get("/interact")
async def interact(text:str):
    wordList = text.lower().split()
    print(text)
    print(wordList)
    print("youtube" in wordList)
    if "youtube" in wordList :
        webbrowser.open("https://youtube.com")
    if "twitter" in wordList:
        webbrowser.open("https://twitter.com")



@app.get("/wikipedia")
async def searchWiki(text:str):
    wordList = text.lower().split()
    index_to_filter = wordList.index("wikipedia")
    webbrowser.open("https://en.wikipedia.org/wiki/"+"".join(wordList[index_to_filter+1:]))