from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_page
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
# from AIC_APP.training.convertCSV import csvData

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
# from .tokens import generate_token

# Create your views here.
def index(request):
    return HttpResponse("shreya")

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
            request.session['username']=username
            # messages.success(request, "Logged In Sucessfully!!")
            return redirect('AIC')
        else:
            messages.error(request, "Bad Credentials!!")
            return render(request, "AIC_APP/login.html")

    return render(request, "AIC_APP/login.html")


def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('signin')


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
            return redirect('signin')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('signin')

        if len(username) > 20:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('signin')

        if pass1 != pass2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('signin')

        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('signin')

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

        return render(request, "AIC_APP/login.html")

    return render(request, "AIC_APP/login.html?signup=true")
