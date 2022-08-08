from ast import pattern
from django.urls import path
from .views import IndexView
urlpatterns = [
path('index/', IndexView.as_view(), name='index'),
]