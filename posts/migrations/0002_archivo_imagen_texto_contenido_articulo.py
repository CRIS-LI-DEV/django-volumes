# Generated by Django 4.2.2 on 2024-02-18 19:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Archivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('archivo', models.FileField(upload_to='archivos/')),
            ],
        ),
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('cover', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Texto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Contenido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Imagen', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='posts.imagen')),
                ('texto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='posts.texto')),
            ],
        ),
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Titulo', models.CharField(max_length=200)),
                ('introduccion', models.TextField()),
                ('publication_date', models.DateTimeField(auto_now_add=True)),
                ('Contenido', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='posts.texto')),
            ],
        ),
    ]
