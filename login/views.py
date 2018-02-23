from django.http import HttpResponse
#from django.shortcuts import render

def index(request):

    return HttpResponse("Tervetuloa N.N-killan kulukorvausjärjestelmään")
#def home(request):
#    return render(request, 'home.html', {})
