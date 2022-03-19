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

curr = os.getcwd()
try:
    # os.chdir(r"C:\Users\patel\PycharmProjects\AIChatBot\AIC\question_generation")
    print(os.getcwd())
    from AIC.question_generation.runnow import runnow
    print("sucesssssssssssssssssssssssssssssssssssssss")

    # os.chdir(r'C:\Users\patel\PycharmProjects\AIChatBot\AIC\OneQueToManyQues')
    from AIC.OneQueToManyQues.main import run_main
    print("sucesssssssssssssssssssssssssssssssssssssss")
    # os.chdir(r"C:\Users\patel\PycharmProjects\AIChatBot\AIC\AIC_APP")
except Exception as e:
    print(f"errrorrrrr{e}")
print(os.getcwd())
try:
    from question_generation.runnow import runnow
    from OneQueToManyQues.main import run_main
except:
    print("still err")



lemmatizer = WordNetLemmatizer()

try:
    intents = json.loads(open(f"{os.getcwd()}{os.sep}AIC_APP{os.sep}training{os.sep}intents.json").read())
    words = pickle.load(open(f"{os.getcwd()}{os.sep}AIC_APP{os.sep}training{os.sep}words.pkl", 'rb'))
    classes = pickle.load(open(f"{os.getcwd()}{os.sep}AIC_APP{os.sep}training{os.sep}classes.pkl", 'rb'))
    model = load_model(f"{os.getcwd()}{os.sep}AIC_APP{os.sep}training{os.sep}modelData{os.sep}chatbotmodel.h5")
except:
    pass

try:
    intents = json.loads(open(f"{os.getcwd()}{os.sep}training{os.sep}intents.json").read())
    words = pickle.load(open(f"{os.getcwd()}{os.sep}training{os.sep}words.pkl", 'rb'))
    classes = pickle.load(open(f"{os.getcwd()}{os.sep}training{os.sep}classes.pkl", 'rb'))
    model = load_model(f"{os.getcwd()}{os.sep}training{os.sep}modelData{os.sep}chatbotmodel.h5")
except Exception:
    pass


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
            result = (i['responses'])
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



def linkingAllFunc():

    with open('C:/Users/patel/PycharmProjects/AIChatBot/AIC/inputText.txt', 'r') as file:
        data = file.read().replace('\n', '')
    if data:
        intentsfile = open('C:/Users/patel/PycharmProjects/AIChatBot/AIC/AIC_APP/static/AIC_APP/intents.json', 'w')

        intentsfile.write('''{
                              "intents": [
                                {
                                  "tag": "Data-0",
                                  "patterns": [],
                                  "responses": ""
                                }
                              ]
                            }''')
        intentsfile.close()
        print("runnow will run")
        print(f"this this this{os.getcwd()}")
        runnow()
        return True
    else:
        return False


def runcombine():

    new_data = []
    resutlLink = linkingAllFunc()
    print(resutlLink)
    if (resutlLink):
        with open('C:/Users/patel/PycharmProjects/AIChatBot/AIC/AIC_APP/static/AIC_APP/intents.json') as json_file:
            data = json.load(json_file)
            temp = data["intents"]
            print(f"this is temp{temp}")
        i = 0
        for entry in temp:
            if i == 0:
                pass
                i += 1
            else:
                new_data.append(entry)
                i += 1
        print(new_data)
        new_dict = {"intents": new_data}
        print(new_dict)
        with open('C:/Users/patel/PycharmProjects/AIChatBot/AIC/AIC_APP/static/AIC_APP/intents.json', "w") as f:
            json.dump(new_dict, f, indent=4)
        print("rich here")
        run_main()
        print("Intent Json file is completely updated..")
    else:
        print("Question Generation is failed")

# for handling the data given by the company xyz
def fetchInputTextArea(request):
    inputText = request.POST.get('inputText', 'default')
    print(inputText)
    file = open('C:/Users/patel/PycharmProjects/AIChatBot/AIC/inputText.txt', 'a')
    file.writelines(inputText)
    file.close()
    runcombine()
    # try:
    #
    return render(request, 'AIC_APP/questionGenerationdisplay.html')
    # except Exception:
    #     return HttpResponse("Some Error Occured")









def QueGenerator(request):
    return render(request, 'AIC_APP/questionGeneration.html')


def questionShow(request):
    runcombine()

    return render(request, 'AIC_APP/questionGenerationdisplay.html')

def improveFeatures(request):
    message = request.POST.get('message', 'hey')
    return HttpResponse("done feedback")

if __name__ == '__main__':
    runcombine()