from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic import CreateView

# Create your views here.

from .models import Autor 
from .models import Books


class AutorsList(ListView):
    template_name = "Library/list-autors.html"
    model = Autor
    context_object_name= 'Autors'

class BooksAutorsList(ListView):
    """Vista para listar libros por autpr"""
    template_name = "Library/list-books.html"
    context_object_name= 'Book'

    def get_queryset(self):
        # identificar el autor
        id = self.kwargs['pk']
        # filtro de libros
        lista = Books.objects.filter(Autor = id)
        # devuelvo el resultado o lista resultado
        return lista

class addAutor(CreateView):
    #vista para registrar un autor
    model = Autor
    template_name = "Library/addAutor.html"
    fields = ['names', 'nationality']
    success_url = '/'

