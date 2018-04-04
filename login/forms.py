from django import forms
from login.models import Document
from django.forms import ModelForm


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('selite', 'korvausdokumentti', 'korvaussumma')
