from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.sessions.models import Session

STATUKSET = (
            ('LAH', 'LÄHETETTY'),
            ('HYV', 'HYVÄKSYTTY'),
            ('HYL', 'HYLÄTTY'),
)

class Document(models.Model):

    selite = models.CharField(max_length=250, blank = True)
    palauttaja = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default = 1)
    palautusaika = models.DateTimeField(auto_now_add=True)
    korvausdokumentti = models.FileField(upload_to='korvaukset/')
    korvaussumma = models.DecimalField(max_digits = 8, decimal_places = 2, default=0)
    status = models.CharField(max_length=3, default = 'LAH', choices = STATUKSET)
