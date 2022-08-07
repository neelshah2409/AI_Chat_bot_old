
import pickle
import nltk
import numpy as np
from keras.models import load_model
from nltk.stem import WordNetLemmatizer
import os


lemmatizer = WordNetLemmatizer()

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    print("sentence_words",sentence_words)
    return sentence_words

def bag_of_words(sentence,id):
    words = pickle.load(open(f"{os.getcwd()}{os.sep}Training{os.sep}words{os.sep}words{id}.pkl", 'rb'))
    sentence_words = clean_up_sentence(sentence)
    print("words is word",words)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1

    return np.array(bag)

def predict_class(sentence,id):
    classes = pickle.load(open(f"{os.getcwd()}{os.sep}Training{os.sep}classes{os.sep}classes{id}.pkl", 'rb'))
    model = load_model(f"{os.getcwd()}{os.sep}Training{os.sep}modelData{os.sep}chatbotmodel{id}.h5")
    bow = bag_of_words(sentence, id)
    print("Bow",bow)
    # res = model.predict(np.array([bow]))[0]
    # np.argmax(res, axis=-1)
    res = model.predict(np.array([bow]), batch_size=32 ,verbose=1)[0]
    # res = model.predict(np.array([bow]), batch_size=32)
    # np.argmax(res, axis=-1)

    print(res)
    # res = model.predict(np.array([bow]))
    print("this is final reessss",res)
    ERROR_THRESHOLD = 0.75
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    print("seprated by space results",results)
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        print(r)
        return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})
    return return_list


def get_response(intent_list, intent_json):
    try:
        print("bababa", intent_list)
        if(len(intent_list) != 0):
            tag = intent_list[0]['intent']
            list_of_intent = intent_json['intents']
            for i in list_of_intent:
                if i['tag'] == tag:
                    result = (i['responses'])
                    break
            return result
        else:
            return "ans prediction list empty"
    except:
        return "No Data Found"
