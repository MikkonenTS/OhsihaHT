from django.urls import path
from django.urls import path, include
from . import views
from .views import *



urlpatterns = [
    path('signup/', views.Signup.as_view(), name='signup'),
    path('upload/', views.upload, name='upload'),
    path('korvaukset/', views.korvaukset, name='korvaukset'),
    path('poista_korvaus/<int:pk>/', views.poista_korvaus, name='poista_korvaus'),

]
