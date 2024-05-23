from django.urls import path
from .views import recognize

urlpatterns = [
    path('recognize/', recognize, name='recognize'),
]
