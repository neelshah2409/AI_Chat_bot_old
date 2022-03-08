from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect


def index(request):
    return HttpResponse("HEY")
# Create your views here.

def harshil(request):
    return render(request, 'AIC_APP/index.html')