import json
import pickle
import nltk
import numpy as np
from django.http import HttpResponse
from django.shortcuts import render
from keras.models import load_model
from nltk.stem import WordNetLemmatizer
import os


# This will help you when you run direct views.py
# try:
#     from AIC.question_generation.runnow import runnow
#     from AIC.question_generation.paraphrase import run_main
#
# except Exception as e:
#     print(f"Error In import Section Views.py{e}")

# try:
#     intents = json.loads(open(f"{os.getcwd()}{os.sep}AIC_APP{os.sep}static{os.sep}AIC_APP{os.sep}intents.json").read())
#     words = pickle.load(open(f"{os.getcwd()}{os.sep}training{os.sep}words.pkl", 'rb'))
#     classes = pickle.load(open(f"{os.getcwd()}{os.sep}training{os.sep}classes.pkl", 'rb'))
#     model = load_model(f"{os.getcwd()}{os.sep}AIC_APP{os.sep}training{os.sep}modelData{os.sep}chatbotmodel.h5")
#
# except Exception:
#     pass



try:
    # djngo server when run so it will accept this pass so ignore the error
    from question_generation.runnow import runnow
    from AIC_APP.training.training import trainTheChatBot
except Exception as e:
    print(f"Error In import Section Views.py{e}")

try:
    from question_generation.paraphrase import run_main
except:
    print("Run main load failed")


lemmatizer = WordNetLemmatizer()

try:
    intents = json.loads(open(f"{os.getcwd()}{os.sep}AIC_APP{os.sep}static{os.sep}AIC_APP{os.sep}intents.json").read())
    words = pickle.load(open(f"{os.getcwd()}{os.sep}AIC_APP{os.sep}training{os.sep}words.pkl", 'rb'))
    classes = pickle.load(open(f"{os.getcwd()}{os.sep}AIC_APP{os.sep}training{os.sep}classes.pkl", 'rb'))
    model = load_model(f"{os.getcwd()}{os.sep}AIC_APP{os.sep}training{os.sep}modelData{os.sep}chatbotmodel.h5")
except Exception as e:
    print(f"Error In import Files Views.py{e}")


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
    list_of_intent = intent_json['intents']
    for i in list_of_intent:
        if i['tag'] == tag:
            result = (i['responses'])
            break

    return result


def index(request):
    return render(request, 'AIC_APP/background.html')


def takeOutputdp(request):
    message = request.POST.get('message', 'hey')
    ints = predict_class(message)
    res = get_response(ints, intents)
    return HttpResponse(res)


def linkingAllFunc():
    with open(f'{os.getcwd()}{os.sep}inputText.txt', 'r') as file:
        data = file.read().replace('\n', '')

    if data:
        intentsfile = open(f'{os.getcwd()}{os.sep}AIC_APP{os.sep}static{os.sep}AIC_APP{os.sep}intents.json', 'w')

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
        print("Question is generating now...")
        runnow()
        return True
    else:
        return False


def runcombine():
    new_data = []
    resutlLink = linkingAllFunc()
    if (resutlLink):
        new_data = []
        with open(f'{os.getcwd()}{os.sep}AIC_APP{os.sep}static{os.sep}AIC_APP{os.sep}intents.json') as json_file:
            data = json.load(json_file)
            temp = data["intents"]
        i = 0
        for entry in temp:
            if i == 0:
                pass
                i += 1
            else:
                new_data.append(entry)
                i += 1
        new_dict = {"intents": new_data}
        with open(f'{os.getcwd()}{os.sep}AIC_APP{os.sep}static{os.sep}AIC_APP{os.sep}intents.json', "w") as f:
            json.dump(new_dict, f, indent=4)

        run_main()
        print("Intent Json file is completely updated..")
    else:
        print("Question Generation is failed")


# for handling the data given by the company xyz
def fetchInputTextArea(request):
    inputText = request.POST.get('inputText', 'default')
    file = open(f'{os.getcwd()}{os.sep}inputText.txt', 'a')
    file.writelines(inputText)
    file.close()
    runcombine()
    return HttpResponse("success")


def QueGenerator(request):
    return render(request, 'AIC_APP/questionGeneration.html')





def improveFeatures(request):
    try:
        messege = request.POST.get('messege', 'default')
        file = open(f'{os.getcwd()}{os.sep}ExtraQuestionForImprovement.txt', 'a')
        file.writelines(messege)
        file.close()
        return HttpResponse("success")
    except Exception as e:
        return HttpResponse("failed")




def QueShow(request):
    return render(request, 'AIC_APP/questionGenerationdisplay.html')


def trainModel(request):
    # try:
    trainTheChatBot()
    return HttpResponse("success")
    # except Exception as e:
    #     return HttpResponse(f"failed {e}")



if __name__ == '__main__':
    runcombine()