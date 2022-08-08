from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
# Create your views here.


# Create your views here.
# Authwiki/views.py

class IndexView(TemplateView):
    success_url = reverse_lazy('login')
    template_name = 'index.html'