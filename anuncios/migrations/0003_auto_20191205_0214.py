# Generated by Django 2.2.7 on 2019-12-05 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anuncios', '0002_auto_20191205_0201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anuncio',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
