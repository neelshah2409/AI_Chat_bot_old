# from AIC.question_generation.pipelines import pipeline
import json
import os
import re
try:
    from question_generation.pipelines import pipeline
except Exception as e:
    print(f"Import pipeline error {e}")


# intentsfile = json.loads(open(f'{os.getcwd()}{os.sep}AIC_APP{os.sep}static{os.sep}AIC_APP{os.sep}intents.json').read())

def write_json(data, filename=f"{os.getcwd()}{os.sep}AIC_APP{os.sep}static{os.sep}AIC_APP{os.sep}intents.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)


def runnow():
    try:
        from question_generation.pipelines import pipeline
    except Exception as e:
        print("pipeline errr")
    import json

    intentsfile = json.loads(open(f'{os.getcwd()}{os.sep}AIC_APP{os.sep}static{os.sep}AIC_APP{os.sep}intents.json').read())

    # nlp = pipeline("multitask-qa-qg")
    nlp = pipeline("question-generation", model="valhalla/t5-small-qg-prepend", ans_model="valhalla/t5-small-qa-qg-hl", qg_format="prepend")


    # to generate questions simply pass the text
    # ans = nlp('''Policies of privatisation should be considered as responses to several distinct pressures. First,
    #  privatisation is a response by the state to internal forces such as increasing fiscal problems (O’Connor, 1973).
    #  It provides a means of lessening the state’s fiscal responsibilities by encouraging the development of private alternatives
    #   which, theoretically at least''')

    with open(f'{os.getcwd()}/inputText', 'r') as file:
        data = file.read().replace('\n', '')
        # print("data is:", data, type(data))
    ans = nlp(data)
    print(f"something{ans}")

    # format of the generation
    # {'answer': 'Twinkal', 'question':'Who is telented", 'answer': 'heuwiehish', 'question':'rhishi, }
    # print(ans)

    anslist = [qa.get('answer') for qa in ans]
    quelist = [qa.get('question') for qa in ans]
    print("heyy", anslist)
    
    sentences = data.split(".")
    full_ans = []
    for i in sentences:
        for j in anslist:
            full_ans.append(i+".") if j.replace("<pad> ","") in i else ""
    print("full ans:: ", full_ans)

    iterate = 0
    for intent in intentsfile['intents']:
        for answer in full_ans:
            print(iterate,len(quelist),len(full_ans))
            list = []
            intent['tag'] = f"Data-{str(iterate + 1)}"
            list.append(quelist[iterate])
            with open(f'{os.getcwd()}/AIC_APP/static/AIC_APP/intents.json') as json_file:
                data = json.load(json_file)
                temp = data["intents"]
                y = {"tag": f"Data-{str(iterate + 1)}", "patterns": list, "responses": answer}
                temp.append(y)
            iterate += 1
            write_json(data)
            print("json data Written ..")

def generatefromOnlyAns(Big_anslist):
    try:
        from question_generation.pipelines import pipeline
    except Exception as e:
        print("pipeline errr")
    import json


    nlp = pipeline("question-generation", model="valhalla/t5-small-qg-prepend", qg_format="prepend")

    updatedQuestionBigList = []
    for ans in Big_anslist:
        ans = nlp(ans)
        quelist = [q.get('question') for q in ans]
        updatedQuestionBigList.append(quelist)

    with open(f'{os.getcwd()}{os.sep}AIC_APP{os.sep}static{os.sep}AIC_APP{os.sep}intents.json') as json_file:
        data = json.load(json_file)
        temp = data["intents"]
        iterate = 1
        length = len(temp)
        for i in updatedQuestionBigList:
            print(i)
            print(i[0])
            y = {"tag": f"Data-{iterate + length}", "patterns": i, "responses": Big_anslist[iterate-1]}
            temp.append(y)
            iterate+=1
        write_json(data)
    print("From OnlyAnser question is generated and updated json file")



if __name__ == '__main__':
    runnow()
    generatefromOnlyAns()
