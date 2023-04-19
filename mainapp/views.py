from django.shortcuts import render
from django.views.generic import TemplateView

class main(TemplateView):
    template_name = "main.html"

