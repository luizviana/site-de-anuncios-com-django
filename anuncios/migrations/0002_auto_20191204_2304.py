# Generated by Django 2.2.7 on 2019-12-05 02:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anuncios', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categoria',
            old_name='categoria_slug',
            new_name='slug',
        ),
    ]
