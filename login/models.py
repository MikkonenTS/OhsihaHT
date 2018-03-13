from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
#from django import forms
#vaihtoehtoisesti tällä, pitäiskö tehä oma forms.py

class Profiles(models.Model):
    """Käyttäjäprofiilien tallennus"""
    #username = models.CharField(max_length=50)
    #miten varmistetaan ettei useampaa samaa, SQL:n avula DB:stä, ID:n avulla?
    #email = models.CharField(max_length=50)
    #firstname = models.CharField(max_length=50)
    #lastname = models.CharField(max_length=50)

class Palautus(models.Model):
    palauttaja = models.CharField(max_length=200)
    palautuspvm = models.DateTimeField('korvauksen pvm')
    #palautustiedosto

#MUISTA, DJANGO LUO ID:N AUTOMAATTISESTI

# Create your models here.
