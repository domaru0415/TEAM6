from django.urls import path
from .views import recognize_speech

urlpatterns = [
    path('recognize/', recognize_speech, name='recognize_speech'),
]
