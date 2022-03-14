from django.http import HttpResponse
import json
import pickle
import random
import nltk
import numpy as np
from django.http import HttpResponse
from django.shortcuts import render
from keras.models import load_model
from nltk.stem import WordNetLemmatizer
import os

lemmatizer = WordNetLemmatizer()

intents = json.loads(open(f"{os.getcwd()}{os.sep}AIC_APP{os.sep}training{os.sep}intents.json").read())
words = pickle.load(open(f"{os.getcwd()}{os.sep}AIC_APP{os.sep}training{os.sep}words.pkl", 'rb'))
classes = pickle.load(open(f"{os.getcwd()}{os.sep}AIC_APP{os.sep}training{os.sep}classes.pkl", 'rb'))
model = load_model(f"{os.getcwd()}{os.sep}AIC_APP{os.sep}training{os.sep}modelData{os.sep}chatbotmodel.h5")

# curr = os.getcwd()
# print(curr)
# intents = json.loads(open(f"{curr}\\training\\intents.json").read())
# words = pickle.load(open(f"{curr}\\training\\words.pkl", 'rb'))
# classes = pickle.load(open(f"{curr}\\training\\classes.pkl", 'rb'))
# model = load_model(f"{curr}\\training\\modelData\\chatbotmodel.h5")


def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words


def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)


def predict_class(sentence):
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})
    return return_list


def get_response(intent_list, intent_json):
    tag = intent_list[0]['intent']
    # print(tag)
    list_of_intent = intent_json['intents']
    # print(list_of_intent)
    for i in list_of_intent:
        if i['tag'] == tag:
            result = random.choice(i['responses'])
            break

    return result


def index(request):
    return render(request, 'AIC_APP/background.html')


def takeOutputdp(request):
    message = request.POST.get('message', 'hey')
    print(message)
    ints = predict_class(message)
    res = get_response(ints, intents)
    print(res)
    # return render(request, 'AIC_APP/index.html')
    return HttpResponse(res)


# for handling the data given by the company xyz
def fetchInputTextArea(request):
    inputText = request.POST.get('inputText', 'default')
    print(inputText)
    file = open('inputText', 'w')

    file.writelines(inputText)
    print('write')
    file.close()
    return HttpResponse("Success")


def QueGenerator(request):
    return render(request, 'AIC_APP/questionGeneration.html')
