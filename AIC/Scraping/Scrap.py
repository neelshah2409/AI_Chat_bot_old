import unicodedata

from bs4 import BeautifulSoup
import requests
import re

def getData(data):
    page = requests.get(data).text
    soup = BeautifulSoup(page,'lxml')

    data = []
    for i in soup.find_all(['p']):
        print(i.text.strip(),"\n")
        data.append(i.text.strip().replace("\n","<br/>").replace("\r",""))

    return data


def getDataWithClass(data,baseClass,questionClass,answerClass):
    page = requests.get(data).text
    soup = BeautifulSoup(page,'lxml')
    questionsData = []
    answerData = []
    for i in soup.select(f".{baseClass} {questionClass}"):
        questionsData.append(f"What is {i.text.strip()}?")
    for i in soup.select(f".{baseClass} {answerClass}"):
        answerData.append(i.text.strip())

    return (questionsData,answerData)