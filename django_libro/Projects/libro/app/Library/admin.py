from django.contrib import admin

# Register your models here.

from .models import Autor
from .models import Books

#clase para mejorar el administrador de autor

class AutorAdmin(admin.ModelAdmin):
    list_display = (
        'names',
        'nationality',
        'id',
    )

    #Atributo para buscar
    search_fields = ('names', 'nationality',)

class BooksAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'resumen',
        'Autor',
        'id',
    )
    #Atributo para buscar
    search_fields = ('title',)

    #para hacer filtros
    list_filter = ('Autor',)


admin.site.register(Autor, AutorAdmin)
admin.site.register(Books, BooksAdmin)