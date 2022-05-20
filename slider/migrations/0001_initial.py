# Generated by Django 4.0.3 on 2022-05-20 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Titulo')),
                ('description', models.TextField(verbose_name='Descripción')),
                ('urlBase', models.CharField(default='https://badaeventos.herokuapp.com', editable=False, max_length=200, verbose_name='API')),
                ('image', models.ImageField(upload_to='slider/images', verbose_name='Imagen')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Slider',
                'verbose_name_plural': 'Slider',
            },
        ),
    ]
