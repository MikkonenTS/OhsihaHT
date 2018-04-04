from django.contrib import admin
from .models import Document

def hyvaksy_korvaus(modeladmin, request, queryset):

    queryset.update(status = 'HYV')
    hyvaksy_korvaus.short_description = "Hyväksy kulukorvaushakemus"

def hylkaa_korvaus(modeladmin, request, queryset):

    queryset.update(status = 'HYL')
    hylkaa_korvaus.short_description = "Hylkää kulukorvaushakemus"

class DocumentAdmin(admin.ModelAdmin):
    list_display = ['status', 'selite', 'palauttaja', 'palautusaika',
    'korvausdokumentti', 'korvaussumma']
    ordering = ['palautusaika']
    actions = [hyvaksy_korvaus, hylkaa_korvaus]

admin.site.register(Document, DocumentAdmin)

# Register your models here.
