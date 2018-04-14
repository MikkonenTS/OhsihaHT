from django.urls import path
from django.urls import path, include
from . import views



urlpatterns = [
    path('signup/', views.Signup.as_view(), name='signup'),
    path('upload/', views.upload, name='upload'),
    path('korvaukset/', views.korvaukset, name='korvaukset'),
    path('poista_korvaus/', views.poista_korvaus, name='poista_korvaus'),


]
