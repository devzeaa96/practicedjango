from django.urls import path
from . import views


app_name = 'Library'

urlpatterns = [
    path('autors', views.AutorsList.as_view(), name="autors"),
    path('books_autors/<pk>/', views.BooksAutorsList.as_view(), name="books_autors"),
        path('autors/add', views.addAutor.as_view(), name="autors/add"),

]