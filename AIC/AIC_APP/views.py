# djngo server when run so it will accept this pass so ignore the error
import json
import os

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.http import HttpResponse, request,JsonResponse

try:
    # djngo server when run so it will accept this pass so ignore the error
    from question_generation.runnow import runnow,generatefromOnlyAns
    from Training.training import trainTheChatBot
    from Predict.predict import *
    from AIC_API.models import Api
    from Scraping.Scrap import getData, getDataWithClass
    from Files.filesConvert import csvData, txtData, docxData
except Exception as e:
    print(f"Error In import Section Views.py{e}")

try:
    from question_generation.paraphrase import run_main, parafromqueans
except Exception as e:
    print(e)
    print("Run main load failed")

# Landing page of website
def index(request):
    if request.method == 'GET':
        return render(request, 'AIC_APP/index.html')
    elif request.method == 'POST':
        try:
            print(request.session['Id'])
            print(request.session['loggedin'])
            if request.session['Id']:
                return render(request, 'AIC_APP/index.html')
        except Exception as e:
            return redirect('signin')


# This two function reset the entire json file....


# for handling the data in form of paragraph given by the company xyz
def fetchInputTextArea(request):
    id = request.session['Id']
    inputText = request.POST.get('inputText', 'default')
    print(inputText)
    runcombine(inputText,id)
    return HttpResponse("success")

# for handling the data(by link) given by the company xyz
def linkSubmit(request):
    id = request.session["Id"]
    data = request.POST.get("link", "default")
    baseClass = request.POST.get("baseClass","")
    questionClass = request.POST.get("questionClass", "")
    answerClass = request.POST.get("answerClass","")
    if(baseClass!=""):
        quelist,anslist = getDataWithClass(data,baseClass,questionClass,answerClass)
        parafromqueans(anslist, quelist, id)
    else:
        siteData = getData(data)
        finalQuelist = generatefromOnlyAns(siteData)
        parafromqueans(siteData, finalQuelist, id)
    print("Sucessfully answering done in json file")
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
    type = request.POST.get("fileType")
    print(type)
    if(type == "csv"):
        fs = FileSystemStorage()
        fname = fs.save(str(id), file)
        fileData = csvData(fs.url(fname))
        fs.delete(str(id))
    elif(type == "txt"):
        fs = FileSystemStorage()
        fname = fs.save(str(id), file)
        fileData = txtData(fs.url(fname))
        fs.delete(str(id))
    elif(type == "docx"):
        fs = FileSystemStorage()
        fname = fs.save(str(id), file)
        fileData = docxData(fs.url(fname))
        fs.delete(str(id))
    else:
        return HttpResponse("error")
    print("done")

    anslist = fileData['answers']
    quelist = fileData['questions']
    if (len(quelist) == len(anslist)):
        print("done1")
        parafromqueans(anslist, quelist,id)
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
        intentsfile = open(f'{os.getcwd()}{os.sep}AIC_APP{os.sep}static{os.sep}AIC_APP{os.sep}intents{os.sep}intents{id}.json', 'w', encoding="utf-8")

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
        with open(f'{os.getcwd()}{os.sep}AIC_APP{os.sep}static{os.sep}AIC_APP{os.sep}intents{os.sep}intents{id}.json', encoding="utf-8") as json_file:
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
        with open(f'{os.getcwd()}{os.sep}AIC_APP{os.sep}static{os.sep}AIC_APP{os.sep}intents{os.sep}intents{id}.json', "w", encoding="utf-8") as f:
            json.dump(new_dict, f, indent=4)

        run_main(id)
        print("Intent Json file is completely updated..")
    else:
        print("Question Generation is failed")

# Question Ans show
def QueShow(request):
    try:
        if request.session['Id']:
            return render(request, 'AIC_APP/questionShow.html')
    except Exception as e:
        return redirect('signin')
    
# Train model
def trainModel(request):
    # try:
    id = request.session['Id']
    trainTheChatBot(id)
    return HttpResponse("success")

# predict ans from input
def takeOutputdp(request):
    id = request.session['Id']
    intents = json.loads(open(f"{os.getcwd()}{os.sep}AIC_APP{os.sep}static{os.sep}AIC_APP{os.sep}intents{os.sep}intents{id}.json",encoding="utf-8").read())
    message = request.POST.get('message', 'hey')
    ints = predict_class(message,id)
    res = get_response(ints, intents)
    return HttpResponse(res)

# this will redirect the page of question generations
def generateFAQs(request):
    try:
        if request.session['Id']:
            return render(request,"AIC_APP/generateFAQs.html")
    except Exception as e:
        return redirect('signin')
    
# Feedback
def improveFeatures(request):
    try:
        messege = request.POST.get('messege', 'default')
        improvementData = Api.objects.filter(api_key='rishi').values()
        context = {"improvementData": improvementData}
        print("this is improvdata",improvementData,context)
        return HttpResponse("success")
    except Exception as e:
        return HttpResponse(f"failed")

def QueGenerator(request):
    try:
        if request.session['Id']:
            return render(request, 'AIC_APP/questionGeneration.html')
    except Exception as e:
        return redirect('signin')
    
def chatAssistant(request):
    try:
        if request.session['Id']:
            return render(request, 'AIC_APP/chatAssistant.html')
    except Exception as e:
        return redirect('signin')
    
def questionAnswers(request):
    try:
        if request.session['Id']:
            return render(request, 'AIC_APP/modules/questionAnswers.html')
    except Exception as e:
        return redirect('signin')
    
def onlyAnswers(request):
    try:
        if request.session['Id']:
            return render(request, 'AIC_APP/modules/onlyAnswers.html')
    except Exception as e:
        return redirect('signin')
    
def linkInput(request):
    try:
        if request.session['Id']:
            return render(request, 'AIC_APP/modules/link.html')
    except Exception as e:
        return redirect('signin')
    
def filesInput(request):
    try:
        if request.session['Id']:
            return render(request, 'AIC_APP/modules/files.html')    
    except Exception as e:
        return redirect('signin')
    
def paragraph(request):
    try:
        if request.session['Id']:
            return render(request, 'AIC_APP/modules/paragraph.html')
    except Exception as e:
        return redirect('signin')

def updateJson(request):
    id = request.session["Id"]
    jsonData = request.POST.get("updateData","default")
    with open(f'{os.getcwd()}{os.sep}AIC_APP{os.sep}static{os.sep}AIC_APP{os.sep}intents{os.sep}intents{id}.json', 'w', encoding="utf-8") as f:
        f.write(jsonData)
    print(jsonData)
    return HttpResponse("success")

def resetAll(request):
    try:
        id=request.session['Id']
        with open(f"{os.getcwd()}{os.sep}AIC_APP{os.sep}static{os.sep}AIC_APP{os.sep}intents{os.sep}intents{id}.json",'w', encoding="utf-8") as f:
            f.write('{"intents": []}')
            return redirect('QueShow')
    except Exception as e:
        return redirect('signin')
    
def getIntentsData(request):

    if 'Id' not in request.session:
        return redirect('signin')
    else:
        id = request.session['Id']
        with open(f"{os.getcwd()}{os.sep}AIC_APP{os.sep}static{os.sep}AIC_APP{os.sep}intents{os.sep}intents{id}.json",'r', encoding="utf-8") as f:
            data = f.read()
            f.close()
        return JsonResponse({"data": data})


if __name__ == '__main__':
    runcombine()