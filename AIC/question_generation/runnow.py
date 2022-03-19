# from AIC.question_generation.pipelines import pipeline
import json

intentsfile = json.loads(open('C:/Users/patel/PycharmProjects/AIChatBot/AIC/AIC_APP/static/AIC_APP/intents.json').read())

def write_json(data, filename="C:/Users/patel/PycharmProjects/AIChatBot/AIC/AIC_APP/static/AIC_APP/intents.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)


def runnow():
    try:
        from question_generation.pipelines import pipeline
    except Exception as e:
        print("pipeline errr")
    import json

    intentsfile = json.loads(open('C:/Users/patel/PycharmProjects/AIChatBot/AIC/AIC_APP/static/AIC_APP/intents.json').read())
    # nlp = pipeline("multitask-qa-qg")
    nlp = pipeline("question-generation", model="valhalla/t5-small-qg-prepend", qg_format="prepend")
    print("here i am ")


    # to generate questions simply pass the text
    ans = nlp('''Policies of privatisation should be considered as responses to several distinct pressures. First,
     privatisation is a response by the state to internal forces such as increasing fiscal problems (O’Connor, 1973).
     It provides a means of lessening the state’s fiscal responsibilities by encouraging the development of private alternatives
      which, theoretically at least''')

    # with open('C:/Users/patel/PycharmProjects/AIChatBot/AIC/inputText.txt', 'r') as file:
    #     data = file.read().replace('\n', '')
    # ans = nlp(data)

    # format of the generation
    # {'answer': 'heuwiehish', 'question':'rhishi, 'answer': 'heuwiehish', 'question':'rhishi, }
    # print(ans)

    anslist = []
    quelist = []
    for qa in ans:
        anslist.append(qa.get('answer'))
        quelist.append(qa.get('question'))

    print("OUR list is: ")
    print(anslist, quelist)

    iterate = 0
    for intent in intentsfile['intents']:
        for answer in anslist:
            list = []
            intent['tag'] = f"Data-{str(iterate + 1)}"
            list.append(quelist[iterate])
            with open('C:/Users/patel/PycharmProjects/AIChatBot/AIC/AIC_APP/static/AIC_APP/intents.json') as json_file:
                data = json.load(json_file)
                temp = data["intents"]
                y = {"tag": f"Data-{str(iterate + 1)}", "patterns": list, "responses": answer}
                temp.append(y)
            iterate +=1
            write_json(data)

if __name__ == '__main__':
    runnow()


class RunNow:
    def __init__(self):
        runnow()