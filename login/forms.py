from django import forms
from login.models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('selite', 'korvausdokumentti', )
