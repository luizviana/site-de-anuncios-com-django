# Generated by Django 2.2.7 on 2019-12-05 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anuncios', '0003_auto_20191205_0214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anuncio',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]