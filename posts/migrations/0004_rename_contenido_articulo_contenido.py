# Generated by Django 4.2.2 on 2024-02-18 19:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_rename_titulo_articulo_titulo_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articulo',
            old_name='Contenido',
            new_name='contenido',
        ),
    ]
