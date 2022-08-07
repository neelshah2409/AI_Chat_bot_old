
import json
from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktParameters
import os
import re
# try:
#     from question_generation.pipelines import pipeline
# except Exception as e:
#     print("pipeline errr")
import json

try:
    from question_generation.pipelines import pipeline
except Exception as e:
    print(f"Import pipeline error {e}")
nlp = pipeline("question-generation", model="valhalla/t5-small-qg-prepend", ans_model="valhalla/t5-small-qa-qg-hl",
                   qg_format="prepend")


def write_json(data,id):
    filename = f"{os.getcwd()}{os.sep}AIC_APP{os.sep}static{os.sep}AIC_APP{os.sep}intents{os.sep}intents{id}.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def givequeanstopara(data,id):
    # try:
    #     from question_generation.pipelines import pipeline
    # except Exception as e:
    #     print("pipeline errr")

    intentsfile = json.loads(open(
        f'{os.getcwd()}{os.sep}AIC_APP{os.sep}static{os.sep}AIC_APP{os.sep}intents{os.sep}intents{id}.json',encoding="utf-8").read(),
                             )

    # nlp = pipeline("multitask-qa-qg")
    # nlp = pipeline("question-generation", model="valhalla/t5-small-qg-prepend", ans_model="valhalla/t5-small-qa-qg-hl",
    #                qg_format="prepend")

    # to generate questions simply pass the text
    # ans = nlp('''Policies of privatisation should be considered as responses to several distinct pressures. First,
    #  privatisation is a response by the state to internal forces such as increasing fiscal problems (O’Connor, 1973).
    #  It provides a means of lessening the state’s fiscal responsibilities by encouraging the development of private alternatives
    #   which, theoretically at least''')

    ans = nlp(data)

    # format of the generation
    # {'answer': 'Twinkal', 'question':'Who is telented", 'answer': 'heuwiehish', 'question':'rhishi, }

    anslist = [qa.get('answer') for qa in ans]
    quelist = [qa.get('question') for qa in ans]

    punkt_para = PunktParameters()
    punkt_para.abbrev_types = set(re.findall('\\b[A-Z](?:[\\.&]?[A-Z]){1,7}\\b', data))
    tokenizer = PunktSentenceTokenizer(punkt_para)
    sentences = tokenizer.tokenize(data)
    full_ans = []
    for i in sentences:
        for j in anslist:
            full_ans.append(i) if j.replace("<pad> ", "") in i else ""

    return full_ans,quelist


def runnow(data,id):
    try:
        from question_generation.pipelines import pipeline
    except Exception as e:
        print("pipeline errr")
    import json

    intentsfile = json.loads(open(f'{os.getcwd()}{os.sep}AIC_APP{os.sep}static{os.sep}AIC_APP{os.sep}intents{os.sep}intents{id}.json', encoding="utf-8").read())

    # nlp = pipeline("multitask-qa-qg")
    nlp = pipeline("question-generation", model="valhalla/t5-small-qg-prepend", ans_model="valhalla/t5-small-qa-qg-hl", qg_format="prepend")


    # to generate questions simply pass the text
    # ans = nlp('''Policies of privatisation should be considered as responses to several distinct pressures. First,
    #  privatisation is a response by the state to internal forces such as increasing fiscal problems (O’Connor, 1973).
    #  It provides a means of lessening the state’s fiscal responsibilities by encouraging the development of private alternatives
    #   which, theoretically at least''')

    ans = nlp(data)

    # format of the generation
    # {'answer': 'Twinkal', 'question':'Who is telented", 'answer': 'heuwiehish', 'question':'rhishi, }

    anslist = [qa.get('answer') for qa in ans]
    quelist = [qa.get('question') for qa in ans]
    
    punkt_para = PunktParameters()
    punkt_para.abbrev_types = set(re.findall('\\b[A-Z](?:[\\.&]?[A-Z]){1,7}\\b', data))
    tokenizer = PunktSentenceTokenizer(punkt_para)
    sentences = tokenizer.tokenize(data)
    full_ans = []
    for i in sentences:
        for j in anslist:
            full_ans.append(i) if j.replace("<pad> ","") in i else ""




    iterate = 0
    for intent in intentsfile['intents']:
        for answer in full_ans:

            list = []
            intent['tag'] = f"Data-{str(iterate + 1)}"
            try:
                list.append(quelist[iterate])
            except:
                pass

            with open(f'{os.getcwd()}/AIC_APP/static/AIC_APP/intents/intents{id}.json', encoding="utf-8") as json_file:
                data = json.load(json_file)
                temp = data["intents"]
                y = {"tag": f"Data-{str(iterate + 1)}", "patterns": list, "responses": answer}
                temp.append(y)
            iterate += 1
            print("upperpart of json written")
            write_json(data,id)
            print("json data Written ..")

def generatefromOnlyAns(Big_anslist):
    # try:
    #     from question_generation.pipelines import pipeline
    # except Exception as e:
    #     print("pipeline errr")


    # nlp = pipeline("question-generation", model="valhalla/t5-small-qg-prepend", qg_format="prepend")

    updatedQuestionBigList = []
    for ans in Big_anslist:
        ans = nlp(ans)
        quelist = [q.get('question') for q in ans]
        updatedQuestionBigList.append(quelist[0])
    # print(f"this is {updatedQuestionBigList}")
    # with open(f'{os.getcwd()}{os.sep}AIC_APP{os.sep}static{os.sep}AIC_APP{os.sep}intents.json') as json_file:
    #     data = json.load(json_file)
    #     temp = data["intents"]
    #     iterate = 1
    #     length = len(temp)
    #     for i in updatedQuestionBigList:
    #         print(i)
    #         print(i[0])
    #         y = {"tag": f"Data-{iterate + length}", "patterns": i, "responses": Big_anslist[iterate-1]}
    #         temp.append(y)
    #         iterate+=1
    #     write_json(data)

    print("From OnlyAnser question is generated and updated json file")
    return updatedQuestionBigList



if __name__ == '__main__':
    runnow()
    generatefromOnlyAns()
    givequeanstopara()
