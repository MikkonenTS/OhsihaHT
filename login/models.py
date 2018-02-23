from django.db import models

#class Profiles(object):
#    """Käyttäjäprofiilien tallennus"""
#    username = models.OneToOneField(USER)
#    email = models.CharField(max_length=50)
#   firstname = models.CharField(max_length=50)
#   lastname = models.CharField(max_length=50)


class Palautus(models.Model):
    palauttaja = models.CharField(max_length=200)
    palautuspvm = models.DateTimeField('korvauksen pvm')
    #palautustiedosto

#MUISTA, DJANGO LUO ID:N AUTOMAATTISESTI

# Create your models here.
