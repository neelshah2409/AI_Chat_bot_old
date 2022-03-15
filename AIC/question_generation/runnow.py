from pipelines import pipeline
import json
intentsfile = json.loads(open('../intents.json').read())


def updatejson(intent):
    a_file = open("../intents.json", "a")
    json.dump(intent ,a_file)
    a_file.write(',')
    a_file.close()



def lastupdateTag():
    a_file = open("../intents.json", "a")
    a_file.write(']}')
    a_file.close()


# nlp = pipeline("multitask-qa-qg")
nlp = pipeline("question-generation", model="valhalla/t5-small-qg-prepend", qg_format="prepend")

# to generate questions simply pass the text
# ans = nlp('''Approval Process 2021-22
# Frequently Asked Questions
# Page | 1
# Q : Where to send the queries related to portal and approval related issues for the approval
# process 2021-22? ''')

with open('../inputText.txt', 'r') as file:
    data = file.read().replace('\n', '')

ans = nlp(data)

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
        intent['patterns'] = list
        list = []
        list.append(answer)
        intent['responses'] =  answer

        iterate +=1

        updatejson(intent)

lastupdateTag()

