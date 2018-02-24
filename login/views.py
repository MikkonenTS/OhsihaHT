from django.http import HttpResponse
from django.shortcuts import render

def index(request):

    return HttpResponse("Tervetuloa, kirjaudu sisään tai rekisteröidy"),

def signup(request):

    #if request.methon = 'POST':

    return render(request,'signup.html')
