from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, render_to_response
from django.urls import reverse_lazy
from django.views import generic
from login.forms import DocumentForm
from django.conf import settings
from .models import Document

def index(request):

    return HttpResponse("Tervetuloa, kirjaudu sisään tai rekisteröidy"),

class Signup(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('')
    template_name = 'signup.html'

def upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'upload.html', {
        'form': form
    })

def korvaukset(request):

    kulukorvaukset = Document.objects.all() #filtterin avulla järjestys ja käyttäjä?

    return render(request, 'korvaukset.html', {'kulukorvaukset':kulukorvaukset})
