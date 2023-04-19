from django.urls import path
from .views import main

urlpatterns = [
    path('', main.as_view(), name="main")
]
