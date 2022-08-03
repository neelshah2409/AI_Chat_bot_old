from django.core.serializers.json import DjangoJSONEncoder

import json
from django.core.serializers import serialize

from django.http import HttpResponse
from django.shortcuts import render, redirect

from AIC_APP.models import Yobotuser
from django.contrib import messages


from django.contrib.auth import authenticate, login, logout


# Create your views here.
def index(request):
    return HttpResponse("shreya")

def signin(request):
    if "Id" not in request.session:
        if request.method == 'POST':
            Email = request.POST['Email']
            pass1 = request.POST['pass1']
            user = Yobotuser.objects.filter(Email=Email, Password=pass1)
            str_data = serialize('json', user, cls=DjangoJSONEncoder)  # Or you don't need to provide the `cls` here because by default cls is DjangoJSONEncoder

            user = json.loads(str_data)
            # user = Yobotuser.objects.all()
            print(user)
            # user = authenticate(Email=Email, Password=pass1)
            print(f"this is user {user}")
            if (user is not None) and len(user)>0:
                print(user)
                request.session['Email']=user[0]['fields']['Email']
                request.session['Id']=user[0]['pk']
                request.session["Name"]=user[0]['fields']['Name']
                request.session['loggedin'] = True
                return redirect('AIC')
            else:
                request.session['loggedin'] = False
                messages.error(request, "Bad Credentials!!")
                return render(request, "AIC_APP/login.html")
        return render(request, "AIC_APP/login.html")
    else:
        return redirect("AIC")



def signout(request):
    request.session['loggedin'] = False
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('AIC')


def signup(request):
    if "Id" not in request.session:

        if request.method == "POST":
            username = request.POST['Name']
            fname = request.POST['ChatBotName']
            lname = request.POST['PhoneNum']
            email = request.POST['Email']
            pass1 = request.POST['Password']
            pass2 = request.POST['Password2']
            companyName = request.POST['CompanyName']

            if Yobotuser.objects.filter(Name=username):
                messages.error(request, "Username already exist! Please try some other username.")
                msg = "Username already exist! Please try some other username."
                context = {"Errmsg":msg}
                return redirect('signin',context)

            if Yobotuser.objects.filter(Email=email).exists():
                messages.error(request, "Email Already Registered!!")
                msg =  "Email Already Registered!!"
                context = {"Errmsg": msg}
                return redirect('signin',context)

            if len(username) > 20:
                messages.error(request, "Username must be under 20 charcters!!")
                msg =  "Username must be under 20 charcters!!"
                context = {"Errmsg": msg}
                return redirect('signin',context)

            if pass1 != pass2:
                messages.error(request, "Passwords didn't matched!!")
                msg =  "Passwords didn't matched!!"
                context = {"Errmsg": msg}
                return redirect('signin',context)

            if not username.isalnum():
                messages.error(request, "Username must be Alpha-Numeric!!")
                msg = "Username must be Alpha-Numeric!!"
                context = {"Errmsg": msg}
                return redirect('signin',context)

            myuser = Yobotuser(Name=username,Password=pass1,Email=email,CompanyName=companyName,PhoneNum=lname,ChatBotName=fname )
            myuser.save()
            messages.success(request,"Your Account has been created succesfully!! Please check your email to confirm your email address in order to activate your account.")

            return redirect('signin')

        return render(request, "AIC_APP/login.html?signup=true")
    else:
        return redirect("AIC")