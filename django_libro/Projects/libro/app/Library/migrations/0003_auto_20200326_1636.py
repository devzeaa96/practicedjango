# Generated by Django 3.0.4 on 2020-03-26 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0002_books'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='resumen',
            field=models.TextField(blank=True, verbose_name='Resumen'),
        ),
    ]