from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from login.forms import DocumentForm, MuutosForm
from django.conf import settings
from .models import Document
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import DeleteView, UpdateView

def index(request):

    return HttpResponse("Tervetuloa, kirjaudu sisään tai rekisteröidy"),

class Signup(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.palauttaja = request.user
            instance.save()
            messages.success(request, 'Tiedoston lataaminen onnistui')

    else:
        form = DocumentForm()
    return render(request, 'upload.html', {
        'form': form
    })

def korvaukset(request):

    kulukorvaukset = Document.objects.filter(palauttaja_id=request.user.id)
    korvaussummat = Document.objects.filter(palauttaja_id=request.user.id).values('korvaussumma')

    total_list=[]
    total = 0

    for summa in korvaussummat:
        total_list.append(list(summa.values()))

    for korvaussumma in total_list:
        for alkio in korvaussumma:
            total += alkio

    template_data = {'kulukorvaukset':kulukorvaukset,
                    'total':total,
                    }

    return render(request, 'korvaukset.html', template_data)

def poista_korvaus(request, pk):
    post = get_object_or_404(Document, pk = pk)
    post.delete()
    return redirect('korvaukset')

class muuta_korvaus(UpdateView):
    template_name = 'document_update_form.html'
    form_class = MuutosForm
    model = Document
    success_url = reverse_lazy('korvaukset')
