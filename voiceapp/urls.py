from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('recognize/', views.speech_to_text, name='recognize_speech'),
]
