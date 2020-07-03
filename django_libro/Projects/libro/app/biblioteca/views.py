from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic import ListView

# Create your views here.

class IndexView (TemplateView):
    #Que una vista procesa los datos y renderiza el resultado en pantalla
    #Siempre nos pedirá un template con el que trabajar
    #Un template es un archivo html
    template_name = 'home/dashboard.html'

class BooksList(ListView):
    template_name = "home/List.html"
    queryset = ['Libro 1', 'Libro 2', 'Libro 3', 'Libro 4']
    context_object_name= 'Books'
