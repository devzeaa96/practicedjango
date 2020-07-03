from django.db import models

# Create your models here.
class Autor(models.Model):
    names = models.CharField('Names', max_length=80)
    nationality = models.CharField('Nacionalidad', blank=True, max_length=100)

    def __str__(self):
        return self.names

class Books(models.Model):
    title = models.CharField('Titulo', blank=False, max_length=50)
    resumen = models.TextField('Resumen', blank=True)
    Autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

