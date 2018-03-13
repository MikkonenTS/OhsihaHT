from django.http import HttpResponse
from django.shortcuts import render
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

def index(request):

    return HttpResponse("Tervetuloa, kirjaudu sisään tai rekisteröidy"),

'''def signup(request):

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home.html')
        else:
            return render(request,'signup.html')'''

class Signup(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('')
    template_name = 'signup.html'
