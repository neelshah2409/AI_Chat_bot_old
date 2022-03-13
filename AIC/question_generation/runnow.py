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
# ans = nlp("Gravity is most accurately described by the general theory of relativity (proposed by Albert Einstein in 1915),\
#  which describes gravity not as a force, but as the curvature of spacetime, caused by the uneven distribution of mass, and \
#  causing masses to move along geodesic lines. The most extreme example of this curvature of spacetime is a black hole, from\
#   which nothing—not even light—can escape once past the black hole's event horizon.[3] However, for most applications, gravity \
#   is well approximated by Newton's law of universal gravitation, which describes gravity as a force causing any two bodies to \
#   be attracted toward each other, with magnitude proportional to the product of their masses and inversely proportional to the\
#    square of the distance between them.Various units are used to express pressure. Some of these derive from a unit of force \
#    divided by a unit of area; the SI unit of pressure, the pascal (Pa), for example, is one newton per square metre (N/m2);\
#     similarly, the pound-force per square inch (psi) is the traditional unit of pressure in the imperial and U.S. customary \
#     systems. Pressure may also be expressed in terms of standard atmospheric pressure; the atmosphere (atm) is equal to this \
#     pressure, and the torr is defined as 1⁄760 of this. Manometric units such as the centimetre of water, millimetre of mercury,\
#      and inch of mercury are used to express pressures in terms of the height of column of a particular fluid in a manometer.")

with open('data.txt', 'r') as file:
    data = file.read().replace('\n', '')

ans = nlp(data)

# [{'answer': '42', 'question': 'What is the answer to life, the universe and everything?'}]
print(ans)

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
        intent['responses'] =  list

        iterate +=1

        # for question in quelist:
        #     intent['patterns'] = question
        #     break
        # intent.udpate('tag') = "index"
        updatejson(intent)

lastupdateTag()


# for intent in intentsfile['intents']:
#     for question in quelist:
#         # intent.udpate('tag') = "index"
#         updatejson(intent)




#
# for intent in intentsfile['intents']:
#     # ques = updatePatterns(intent.get('patterns')[0])
#     # for i in ques:
#     #     print(i)
#     #     intent.get('patterns').append(i)
#     print(intent.get('patterns'))
#     updatejson(intent)
#     print('done')



# print(f"ans is {ans[0].get('answer')}")
# print(f"Que  is {ans[0].get('question')}")
# for qa pass a dict with "question" and "context"
# nlp({
#     "question": "What is 42 ?",
#     "context": "42 is the answer to life, the universe and everythi\
#     ng."
# })
# 'the answer to life, the universe and everything'
