# djngo server when run so it will accept this pass so ignore the error
import json
import os

from django.core.files.storage import FileSystemStorage
from Files.filesConvert import csvData, txtData, docxData
from django.shortcuts import render, redirect
from Scraping.Scrap import getData,getDataWithClass,getDataWithAnsClass
from django.http import HttpResponse, request,JsonResponse
from rest_framework.parsers import JSONParser

from googletrans import Translator,LANGUAGES
translator = Translator(service_urls=['translate.googleapis.com'])
try:
    # djngo server when run so it will accept this pass so ignore the error
    from question_generation.runnow import runnow,generatefromOnlyAns,givequeanstopara
    from Training.training import trainTheChatBot
    from Predict.predict import *
    from AIC_API.models import Api
    from AIC_API.serializers import ApiSerialize
    from AIC_APP.models import Yobotuser

except Exception as e:
    print(f"Error In import Section Views.py{e}")

try:
    from question_generation.paraphrase import run_main, parafromqueans
except Exception as e:
    print(e)
    print("Run main load failed")




# data come from form ......from js
def setgreeterrmsg(request):

    try:
        id = request.session["Id"]
        greet = request.POST.get("greet")
        err = request.POST.get("sorry")
        print(greet,err)
        Yobotuser.objects.filter(id=id).update(greetmsg = greet, errmsg = err)
        return HttpResponse(f"greet - {greet}& err- {err}")
    except:
        return HttpResponse("failed")

# data send to js file for display in chatbot
def getgreeterrmsg(request):
    try:
        id = request.session['Id']
        entry = Yobotuser.objects.filter(id = "id").values()
        for i in entry:
            greet =i['greetmsg']
            err =i['errmsg']
        data = {"greet": greet, "error":err}
        # return HttpResponse(data)
        print(data)
        return JsonResponse(data)

    except:
        return HttpResponse("failed")


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
# for handling the data(para) given by the company xyz
def fetchInputTextArea(request):
    id = request.session['Id']
    inputText = request.POST.get('inputText', 'default')
    print(inputText)
    anslist,quelist = givequeanstopara(inputText, id)
    # runcombine(inputText,id)
    parafromqueans(anslist, quelist, id)
    return HttpResponse("success")

# for handling the data(by link) given by the company xyz
def linkSubmit(request):
    id = request.session["Id"]
    data = request.POST.get("link", "default")
    baseClass = request.POST.get("baseClass","")
    questionClass = request.POST.get("questionClass", "")
    answerClass = request.POST.get("answerClass","")
    if baseClass!="":
        quelist,anslist = getDataWithClass(data,baseClass,questionClass,answerClass)
        parafromqueans(anslist, quelist, id)
    elif questionClass!="":
        anslist =getDataWithAnsClass()
        finalQuelist = generatefromOnlyAns(anslist)
        parafromqueans(anslist, finalQuelist, id)
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
# def linkingAllFunc(data,id):
#     if data:
#         intentsfile = open(f'{os.getcwd()}{os.sep}AIC_APP{os.sep}static{os.sep}AIC_APP{os.sep}intents{os.sep}intents{id}.json', 'w')
#
#         intentsfile.write('''{
#                               "intents": [
#                                 {
#                                   "tag": "Data-0",
#                                   "patterns": [],
#                                   "responses": ""
#                                 }
#                               ]
#                             }''')
#         intentsfile.close()
#         print("Question is generating now...")
#         runnow(data, id)
#         return True
#     else:
#         return False


# this function working for paraphrasing and reformate function call if require
# def runcombine(data, id):
#
#     new_data = []
#     resutlLink = linkingAllFunc(data, id)
#
#     if (resutlLink):
#         new_data = []
#         with open(f'{os.getcwd()}{os.sep}AIC_APP{os.sep}static{os.sep}AIC_APP{os.sep}intents{os.sep}intents{id}.json') as json_file:
#             data = json.load(json_file)
#             print(f"this is mhaa data------------{data}")
#             temp = data["intents"]
#         i = 0
#         for entry in temp:
#             if i == 0:
#                 i += 1
#             else:
#                 new_data.append(entry)
#                 i += 1
#         new_dict = {"intents": new_data}
#         print(f"this is new dict --------------------------------------------------------{new_dict}")
#         with open(f'{os.getcwd()}{os.sep}AIC_APP{os.sep}static{os.sep}AIC_APP{os.sep}intents{os.sep}intents{id}.json', "w") as f:
#             json.dump(new_dict, f, indent=4)
#
#         run_main(id)
#         print("Intent Json file is completely updated..")
#     else:
#         print("Question Generation is failed")
#

# Question Ans show


def QueShow(request):
    try:
        if request.session['Id']:
            return render(request, 'AIC_APP/questionShow.html')
    except Exception as e:
        return redirect('signin')
    

#api page
def api(request):
        return render(request, 'AIC_APP/API.html')

# Train model
def trainModel(request):
    # try:
    id = request.session['Id']
    trainTheChatBot(id)
    return HttpResponse("success")



# predict ans from input
def takeOutputdp(request):
    id = request.session['Id']
    intents = json.loads(open(f"{os.getcwd()}{os.sep}AIC_APP{os.sep}static{os.sep}AIC_APP{os.sep}intents{os.sep}intents{id}.json", encoding="utf-8").read())
    message = request.POST.get('message', 'hey')
    ints = predict_class(message,id)
    res = get_response(ints, intents)
    # destination = request.POST.get("destination")
    # res = translator.translate(res, src="en", dest=destination).text
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
    # try:
    messege = request.POST.get('messege', 'default')
    # improvementData = Api.objects.filter(api_key='rishi').values()
    # context = {"improvementData": improvementData}
    # api = Api.objects.get(api_key=request.GET.get("api"))
    api = Api.objects.get(api_key="aJ0F7J0P.dGcWDnK5kWPQiCeQgUnsIVqBsy50GYsn")
    serializer = ApiSerialize(api, many=False)
    if api.active == True:
        id = serializer.data['user_id']
        print("this is id ",id)
        oldimprovedata = Yobotuser.objects.only("improvedata").values()
        for i in oldimprovedata:
            print(i['improvedata'])
            oldimprovedata =i['improvedata']
        # print(oldimprovedata['improvedata'])
        # print(oldimprovedata)
        entry = Yobotuser.objects.filter(id= id).update(improvedata=oldimprovedata + " | " +messege)
        # print("this is entry ",entry)
        # entry.improvedata = messege
        # entry.save()

        # file = open(f'{os.getcwd()}{os.sep}ExtraQuestionForImprovement', 'a')
        # file.writelines(messege)
        # file.close()
        # print("this is improvdata",improvementData,context)
        return HttpResponse("success")
    # except Exception as e:
    #     return HttpResponse(f"failed")


def QueGenerator(request):
    try:
        if request.session['Id']:
            return render(request, 'AIC_APP/questionGeneration.html')
    except Exception as e:
        return redirect('signin')
    

def chatAssistant(request):
    try:
        if request.session['Id']:
            return render(request, 'AIC_APP/chatAssistant.html',{"languages":LANGUAGES})
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
    







# def Showdatafromdb(request):
#     # section_id = 1
#     # fetch = Question_ans.objects.all()
#     # fetch = Question_ans.objects.get(questions = "what is this?")
#     new_question = "Is is my connection is complete or not?"
#     query = f'''INSERT INTO `yobot`.`aic_app_question_ans`(`questions`) VALUES ("{new_question}");'''
#     # query = f'''(Insert into aic_app_question_ans values(%s, %s)",['{1}','{new_question}']);'''
#     # fetch = Question_ans.objects.raw("SELECT * FROM aic_app_question_ans")
#     # try:
#     #     Question_ans.objects.raw(f"INSERT INTO `yobot`.`aic_app_question_ans`(`questions`) VALUES ('{new_question}');")
#     #     fetch = Question_ans.objects.raw("SELECT * FROM aic_app_question_ans")
#     #     print(fetch)
#     #     # print(fetch[0].answers)
#     #     # print(fetch[0].questions)
#     #     # ans_que = [(fetch.questions) for fetch in fetch]
#     #     # print(ans_que)
#     # except:
#     #     print("error now")
#
#     with connection.cursor() as cursor:
#         cursor.execute(f"INSERT INTO `yobot`.`aic_app_question_ans`(`questions`) VALUES ('{new_question}');")
#     return HttpResponse("yeah")

def updateJson(request):
    id = request.session["Id"]
    jsonData = request.POST.get("updateData","default")
    with open(f'{os.getcwd()}{os.sep}AIC_APP{os.sep}static{os.sep}AIC_APP{os.sep}intents{os.sep}intents{id}.json', 'w', encoding="utf-8") as f:
        f.write(jsonData)
    print(jsonData)
    return HttpResponse("success")

#
# def getSuggestions(request):
#     suggestionString = request.POST.get("messege", "default")
#     print("SELECT * FROM aic_app_question_ans WHERE questions LIKE '"+suggestionString+"%' LIMIT 3")
#     fetch = Question_ans.objects.raw("SELECT * FROM aic_app_question_ans WHERE questions LIKE 'Wh%' LIMIT 3")
#     suggest = []
#     for i in fetch:
#         suggest.append(i.questions[:])
#     return HttpResponse(str({"suggestions":suggest}))


# def filesConvert(request):
#     # csvPath = request.POST.get("file","default")
#     csvPathFile = request.FILES('file')
#     print(csvPathFile)
#     # siteData = csvData(csvPath)
#     # print(siteData)
#
#     return HttpResponse("success")




# def filesConvert(request):
#     # csvPath = request.POST.get("file","default")
#     # csvPathFile = request.FILES('file')
#     # print(csvPathFile)
#     # # from AIC_APP.training.filesConvert import csvData
#     # # siteData = csvData(csvPath)
#     # # print(siteData)
#     #
#     # return HttpResponse("success")
#     return render(request,  'AIC_APP/csv_upload.html')




# def Gotoauth(request):
#     return render(request, "AIC_APP/login.html")


# def signup(request):
#     if request.method == "POST":
#         username = request.POST['username']
#         fname = request.POST['fname']
#         lname = request.POST['lname']
#         email = request.POST['email']
#         pass1 = request.POST['pass1']
#         pass2 = request.POST['pass2']
#
#         if User.objects.filter(username=username):
#             messages.error(request, "Username already exist! Please try some other username.")
#             return redirect('Gotoauth')
#
#         if User.objects.filter(email=email).exists():
#             messages.error(request, "Email Already Registered!!")
#             return redirect('Gotoauth')
#
#         if len(username) > 20:
#             messages.error(request, "Username must be under 20 charcters!!")
#             return redirect('Gotoauth')
#
#         if pass1 != pass2:
#             messages.error(request, "Passwords didn't matched!!")
#             return redirect('Gotoauth')
#
#         if not username.isalnum():
#             messages.error(request, "Username must be Alpha-Numeric!!")
#             return redirect('Gotoauth')
#
#         myuser = User.objects.create_user(username, email, pass1)
#         myuser.first_name = fname
#         myuser.last_name = lname
#         # myuser.is_active = False
#         myuser.is_active = False
#         myuser.save()
#         messages.success(request,"Your Account has been created succesfully!! Please check your email to confirm your email address in order to activate your account.")
#
#         # # Welcome Email
#         # subject = "Welcome to GFG- Django Login!!"
#         # message = "Hello " + myuser.first_name + "!! \n" + "Welcome to GFG!! \nThank you for visiting our website\n. We have also sent you a confirmation email, please confirm your email address. \n\nThanking You\nAnubhav Madhav"
#         # from_email = settings.EMAIL_HOST_USER
#         # to_list = [myuser.email]
#         # send_mail(subject, message, from_email, to_list, fail_silently=True)
#         #
#         # # Email Address Confirmation Email
#         # current_site = get_current_site(request)
#         # email_subject = "Confirm your Email @ GFG - Django Login!!"
#         # message2 = render_to_string('email_confirmation.html', {
#         #
#         #     'name': myuser.first_name,
#         #     'domain': current_site.domain,
#         #     'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
#         #     'token': generate_token.make_token(myuser)
#         # })
#         # email = EmailMessage(
#         #     email_subject,
#         #     message2,
#         #     settings.EMAIL_HOST_USER,
#         #     [myuser.email],
#         # )
#         # email.fail_silently = True
#         # email.send()
#
#         return render(request, "AIC_APP/login.html")
#
#     return render(request, "AIC_APP/login.html?signup=true")


# def activate(request, uidb64, token):
#     try:
#         uid = force_str(urlsafe_base64_decode(uidb64))
#         myuser = User.objects.get(pk=uid)
#     except (TypeError, ValueError, OverflowError, User.DoesNotExist):
#         myuser = None
#
#     if myuser is not None and generate_token.check_token(myuser, token):
#         myuser.is_active = True
#         # user.profile.signup_confirmation = True
#         myuser.save()
#         login(request, myuser)
#         messages.success(request, "Your Account has been activated!!")
#         return redirect('login')
#     else:
#         return render(request, 'activation_failed.html')


# def signin(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         pass1 = request.POST['pass1']
#
#         user = authenticate(username=username, password=pass1)
#         print(user)
#         if user is not None:
#             login(request, user)
#             fname = user.first_name
#             print(fname)
#             request.session['username']=username
#             # messages.success(request, "Logged In Sucessfully!!")
#             return redirect('Home')
#         else:
#             messages.error(request, "Bad Credentials!!")
#             return render(request, "AIC_APP/login.html")
#
#     return render(request, "AIC_APP/login.html")


# def signout(request):
#     logout(request)
#     messages.success(request, "Logged Out Successfully!!")
#     return redirect('Gotoauth')

def resetAll(request):
    try:
        id=request.session['Id']
        with open(f"{os.getcwd()}{os.sep}AIC_APP{os.sep}static{os.sep}AIC_APP{os.sep}intents{os.sep}intents{id}.json",'w', encoding='utf-8') as f:
            f.write('{"intents": []}')
            return redirect('QueShow')
    except Exception as e:
        return redirect('signin')
    
def getIntentsData(request):

    if 'Id' not in request.session:
        return redirect('signin')
    else:
        id = request.session['Id']
        with open(f"{os.getcwd()}{os.sep}AIC_APP{os.sep}static{os.sep}AIC_APP{os.sep}intents{os.sep}intents{id}.json",'r',encoding='utf-8') as f:
            data = f.read()
            f.close()
        return JsonResponse({"data": data})

def getUserData(request):
    if "Id" not in request.session.keys():
        return redirect('signin')
    else:
        from .models import Yobotuser
        from .serializers import YobotuserSerialize
        user = Yobotuser.objects.get(id=request.session["Id"])
        serialize = YobotuserSerialize(user, many=False)
        return JsonResponse({"status":"success","data": serialize.data})

def updateUserData(request):
    if "Id" not in request.session.keys():
        return redirect('signin')
    else:
        from .models import Yobotuser
        from .serializers import YobotuserSerialize
        data = JSONParser().parse(request)
        user = Yobotuser.objects.get(id=request.session["Id"])
        user.Name = data["name"]
        user.Email = data["email"]
        user.CompanyName = data["organization"]
        user.PhoneNum = data["mobile"]
        user.save()
        request.session["Name"] = data["name"]
        serializer = YobotuserSerialize(user, many=False)
        return JsonResponse({"status":"success","data": serializer.data})

def translate(request):
    message = request.POST.get("message")
    source = request.POST.get("source")
    destination = request.POST.get("destination")
    return JsonResponse({"status": "success", "message": translator.translate(message, src=source, dest=destination).text})

def documentation(request):
    return render(request,"AIC_APP/documentation.html")

# if __name__ == '__main__':
#     # runcombine()

