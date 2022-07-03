import json
import pickle
import nltk
import numpy as np
from django.http import HttpResponse
from django.shortcuts import render, redirect
from keras.models import load_model
from nltk.stem import WordNetLemmatizer
import os
from django.db import connection
from django.core.files.storage import FileSystemStorage
from AIC_APP.training.convertCSV import csvData

from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import EmailMessage, send_mail
# from geeksforgeeks import settings
# from AIC.AIC import settings
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth import authenticate, login, logout
from .tokens import generate_token





import pandas as pd
import csv , io
# This is for db connection you should use this as a db insertion and updation
from .models import Question_ans


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
    from question_generation.runnow import runnow,generatefromOnlyAns
    from AIC_APP.training.training import trainTheChatBot
except Exception as e:
    print(f"Error In import Section Views.py{e}")

try:
    from question_generation.paraphrase import run_main, parafromqueans
except Exception as e:
    print(e)
    print("Run main load failed")


lemmatizer = WordNetLemmatizer()

# try:
#     words = pickle.load(open(f"{os.getcwd()}{os.sep}AIC_APP{os.sep}training{os.sep}words.pkl", 'rb'))
#     classes = pickle.load(open(f"{os.getcwd()}{os.sep}AIC_APP{os.sep}training{os.sep}classes.pkl", 'rb'))
#     model = load_model(f"{os.getcwd()}{os.sep}AIC_APP{os.sep}training{os.sep}modelData{os.sep}chatbotmodel.h5")
# except Exception as e:
#     print(f"Error In import Files Views.py{e}")


def mainPage(request):
    return render(request, 'AIC_APP/mainPage.html')

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words


def bag_of_words(sentence):
    words = pickle.load(open(f"{os.getcwd()}{os.sep}AIC_APP{os.sep}training{os.sep}words.pkl", 'rb'))

    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)


def predict_class(sentence):
    classes = pickle.load(open(f"{os.getcwd()}{os.sep}AIC_APP{os.sep}training{os.sep}classes.pkl", 'rb'))
    model = load_model(f"{os.getcwd()}{os.sep}AIC_APP{os.sep}training{os.sep}modelData{os.sep}chatbotmodel.h5")
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        print(r)
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
    return render(request, 'AIC_APP/index.html')


def takeOutputdp(request):
    intents = json.loads(open(f"{os.getcwd()}{os.sep}AIC_APP{os.sep}static{os.sep}AIC_APP{os.sep}intents.json").read())
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
    print(inputText)
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

def Showdatafromdb(request):
    # section_id = 1
    # fetch = Question_ans.objects.all()
    # fetch = Question_ans.objects.get(questions = "what is this?")
    new_question = "Is is my connection is complete or not?"
    query = f'''INSERT INTO `yobot`.`aic_app_question_ans`(`questions`) VALUES ("{new_question}");'''
    # query = f'''(Insert into aic_app_question_ans values(%s, %s)",['{1}','{new_question}']);'''
    # fetch = Question_ans.objects.raw("SELECT * FROM aic_app_question_ans")
    # try:
    #     Question_ans.objects.raw(f"INSERT INTO `yobot`.`aic_app_question_ans`(`questions`) VALUES ('{new_question}');")
    #     fetch = Question_ans.objects.raw("SELECT * FROM aic_app_question_ans")
    #     print(fetch)
    #     # print(fetch[0].answers)
    #     # print(fetch[0].questions)
    #     # ans_que = [(fetch.questions) for fetch in fetch]
    #     # print(ans_que)
    # except:
    #     print("error now")

    with connection.cursor() as cursor:
        cursor.execute(f"INSERT INTO `yobot`.`aic_app_question_ans`(`questions`) VALUES ('{new_question}');")
    return HttpResponse("yeah")

def updateJson(request):
    jsonData = request.POST.get("updateData","default")
    intentsfile = open(f'{os.getcwd()}{os.sep}AIC_APP{os.sep}static{os.sep}AIC_APP{os.sep}intents.json', 'w')
    intentsfile.write(jsonData)
    return HttpResponse("success")

def onlyAnswersData(request):
    answers = request.POST.get("inputText","default")
    answers = json.loads(answers)
    print(type(answers))
    # {'answers': ['I am rishi patel', 'i am patel rishi']}
    print(answers)
    anslist = [ans for ans in answers['answers']]
    generatefromOnlyAns(anslist)
    print("Sucessfully answering done in json file")
    return HttpResponse("success")

def questionAnswerData(request):
    questionAnswer = request.POST.get("inputText","default")
    jsonquesans = json.loads(questionAnswer)
    anslist = [ans for ans in jsonquesans['answers']]
    quelist = [que for que in jsonquesans['questions']]
    parafromqueans(anslist, quelist)
    print("Sucessfully paraphrasing done in json file")
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

def linkSubmit(request):
    from AIC_APP.training.Scrap import getData
    data = request.POST.get("link", "default")
    siteData = getData(data)
    print(siteData)
    file = open(f'{os.getcwd()}{os.sep}siteData.txt', 'a')
    file.writelines(siteData)
    file.close()
    runcombine()
    return HttpResponse("success")

# def convertCsv(request):
#     # csvPath = request.POST.get("file","default")
#     csvPathFile = request.FILES('file')
#     print(csvPathFile)
#     # siteData = csvData(csvPath)
#     # print(siteData)
#
#     return HttpResponse("success")


def csvSubmit(request):
    file = request.FILES.get("csvfile")
    fs = FileSystemStorage()
    fname = fs.save(file.name, file)
    siteData = csvData(fs.url(fname))
    print(siteData)
    return HttpResponse(fs.url(fname))



def convertCsv(request):
    # csvPath = request.POST.get("file","default")
    # csvPathFile = request.FILES('file')
    # print(csvPathFile)
    # # from AIC_APP.training.convertCSV import csvData
    # # siteData = csvData(csvPath)
    # # print(siteData)
    #
    # return HttpResponse("success")
    return render(request,  'AIC_APP/csv_upload.html')




def Gotoauth(request):
    return render(request, "AIC_APP/login.html")


def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('Gotoauth')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('Gotoauth')

        if len(username) > 20:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('Gotoauth')

        if pass1 != pass2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('Gotoauth')

        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('Gotoauth')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        # myuser.is_active = False
        myuser.is_active = False
        myuser.save()
        messages.success(request,"Your Account has been created succesfully!! Please check your email to confirm your email address in order to activate your account.")

        # # Welcome Email
        # subject = "Welcome to GFG- Django Login!!"
        # message = "Hello " + myuser.first_name + "!! \n" + "Welcome to GFG!! \nThank you for visiting our website\n. We have also sent you a confirmation email, please confirm your email address. \n\nThanking You\nAnubhav Madhav"
        # from_email = settings.EMAIL_HOST_USER
        # to_list = [myuser.email]
        # send_mail(subject, message, from_email, to_list, fail_silently=True)
        #
        # # Email Address Confirmation Email
        # current_site = get_current_site(request)
        # email_subject = "Confirm your Email @ GFG - Django Login!!"
        # message2 = render_to_string('email_confirmation.html', {
        #
        #     'name': myuser.first_name,
        #     'domain': current_site.domain,
        #     'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
        #     'token': generate_token.make_token(myuser)
        # })
        # email = EmailMessage(
        #     email_subject,
        #     message2,
        #     settings.EMAIL_HOST_USER,
        #     [myuser.email],
        # )
        # email.fail_silently = True
        # email.send()

        return redirect('login')

    return render(request, "AIC_APP/login.html?signup=true")


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        myuser = None

    if myuser is not None and generate_token.check_token(myuser, token):
        myuser.is_active = True
        # user.profile.signup_confirmation = True
        myuser.save()
        login(request, myuser)
        messages.success(request, "Your Account has been activated!!")
        return redirect('login')
    else:
        return render(request, 'activation_failed.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)
        print(user)
        if user is not None:
            login(request, user)
            fname = user.first_name
            print(fname)
            # messages.success(request, "Logged In Sucessfully!!")
            return redirect('Home')
        else:
            messages.error(request, "Bad Credentials!!")
            return render(request, "AIC_APP/login.html")

    return render(request, "AIC_APP/login.html")


def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('Gotoauth')

if __name__ == '__main__':
    runcombine()

