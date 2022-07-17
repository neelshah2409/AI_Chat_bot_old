# djngo server when run so it will accept this pass so ignore the error
import json

from django.core.files.storage import FileSystemStorage
from AIC_APP.training.convertCSV import csvData
from django.shortcuts import render, redirect


from django.http import HttpResponse, request


try:
    # djngo server when run so it will accept this pass so ignore the error
    from question_generation.runnow import runnow,generatefromOnlyAns
    from AIC_APP.training.training import trainTheChatBot
    from Predict.predict import *
except Exception as e:
    print(f"Error In import Section Views.py{e}")

try:
    from question_generation.paraphrase import run_main, parafromqueans
except Exception as e:
    print(e)
    print("Run main load failed")





# Landing page of website
def index(request):
    print(request.session['Id'])
    print(request.session['loggedin'])
    if (request.session['loggedin'] and request.session['Id']):
        return render(request, 'AIC_APP/index.html')
    else:
        return redirect('signin')





# This two function reset the entire json file....
# for handling the data(para) given by the company xyz
def fetchInputTextArea(request):
    id = request.session['Id']
    inputText = request.POST.get('inputText', 'default')
    print(inputText)
    runcombine(inputText,id)
    return HttpResponse("success")

# for handling the data(by link) given by the company xyz
def linkSubmit(request):
    from AIC_APP.training.Scrap import getData
    id = request.session["Id"]
    data = request.POST.get("link", "default")
    questionClass = request.POST.get("questionClass", "")
    answerClass = request.POST.get("answerClass","")
    siteData = getData(data)
    print(siteData)
    runcombine(siteData, id)
    return HttpResponse("success")


















# This three function append the json file....

# for handling the data(pre built que ans format) given by the company xyz
def questionAnswerData(request):
    id = request.session['Id']
    questionAnswer = request.POST.get("inputText","default")
    jsonquesans = json.loads(questionAnswer)
    anslist = [ans for ans in jsonquesans['answers']]
    quelist = [que for que in jsonquesans['questions']]
    parafromqueans(anslist, quelist,id)
    print("Sucessfully paraphrasing done in json file")
    return HttpResponse("success")

# for handling the data(CSV DOC TEXT FILE INPUT) given by the company xyz
def fileSubmit(request):
    id = request.session['Id']
    file = request.FILES.get("fileInput")
    print(file)
    fs = FileSystemStorage()
    fname = fs.save(str(id), file)
    siteData = csvData(fs.url(fname))
    print(siteData)
    anslistfromcsv = siteData['answers']
    quelistfromcsv = siteData['questions']
    if (len(anslistfromcsv) == len(quelistfromcsv)):
        parafromqueans(anslistfromcsv, quelistfromcsv,id)
    else:
        return (HttpResponse("Csv File contain unstructured data please check the again"))
    return HttpResponse(fs.url(fname))

# for handling the data(Only answer format) given by the company xyz
def onlyAnswersData(request):
    id = request.session['Id']
    answers = request.POST.get("inputText","default")
    answers = json.loads(answers)
    print(type(answers))
    print(answers)
    anslist = [ans for ans in answers['answers']]
    finalQuelist = generatefromOnlyAns(anslist)
    parafromqueans(anslist, finalQuelist,id)
    print("Sucessfully answering done in json file")
    return HttpResponse("success")









# This function is reformat the json file if require
def linkingAllFunc(data,id):
    if data:
        intentsfile = open(f'{os.getcwd()}{os.sep}AIC_APP{os.sep}static{os.sep}AIC_APP{os.sep}intents{os.sep}intents{id}.json', 'w')

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
        runnow(data, id)
        return True
    else:
        return False


# this function working for paraphrasing and reformate function call if require
def runcombine(data, id):

    new_data = []
    resutlLink = linkingAllFunc(data, id)

    if (resutlLink):
        new_data = []
        with open(f'{os.getcwd()}{os.sep}AIC_APP{os.sep}static{os.sep}AIC_APP{os.sep}intents{os.sep}intents{id}.json') as json_file:
            data = json.load(json_file)
            print(f"this is mhaa data------------{data}")
            temp = data["intents"]
        i = 0
        for entry in temp:
            if i == 0:
                i += 1
            else:
                new_data.append(entry)
                i += 1
        new_dict = {"intents": new_data}
        print(f"this is new dict --------------------------------------------------------{new_dict}")
        with open(f'{os.getcwd()}{os.sep}AIC_APP{os.sep}static{os.sep}AIC_APP{os.sep}intents{os.sep}intents{id}.json', "w") as f:
            json.dump(new_dict, f, indent=4)

        run_main(id)
        print("Intent Json file is completely updated..")
    else:
        print("Question Generation is failed")


# Question Ans show
def QueShow(request):
    return render(request, 'AIC_APP/questionShow.html')

# Train model
def trainModel(request):
    # try:
    id = request.session['Id']
    trainTheChatBot(id)
    return HttpResponse("success")



# predict ans from input
def takeOutputdp(request):
    id = request.session['Id']
    intents = json.loads(open(f"{os.getcwd()}{os.sep}AIC_APP{os.sep}static{os.sep}AIC_APP{os.sep}intents{os.sep}intents{id}.json").read())
    message = request.POST.get('message', 'hey')
    ints = predict_class(message,id)
    res = get_response(ints, intents)
    return HttpResponse(res)

# this will redirect the page of question generations
def generateFAQs(request):
    return render(request,"AIC_APP/generateFAQs.html")











































# Feedback
def improveFeatures(request):
    try:
        messege = request.POST.get('messege', 'default')
        file = open(f'{os.getcwd()}{os.sep}ExtraQuestionForImprovement', 'a')
        file.writelines(messege)
        file.close()
        return HttpResponse("success")
    except Exception as e:
        return HttpResponse(f"failed")


def QueGenerator(request):
    return render(request, 'AIC_APP/questionGeneration.html')

def chatAssistant(request):
    return render(request, 'AIC_APP/chatAssistant.html')

def questionAnswers(request):
    return render(request, 'AIC_APP/modules/questionAnswers.html')

def onlyAnswers(request):
    return render(request, 'AIC_APP/modules/onlyAnswers.html')

def linkInput(request):
    return render(request, 'AIC_APP/modules/link.html')

def filesInput(request):
    return render(request, 'AIC_APP/modules/files.html')

def paragraph(request):
    return render(request, 'AIC_APP/modules/paragraph.html')

if __name__ == '__main__':
    runcombine()

