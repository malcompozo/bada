# Generated by Django 4.0.3 on 2022-05-18 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('email', models.EmailField(max_length=100, verbose_name='Email')),
                ('message', models.CharField(max_length=250, verbose_name='Mensaje')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
            ],
            options={
                'verbose_name': 'Contacto',
                'verbose_name_plural': 'Contacto',
                'ordering': ['-created'],
            },
        ),
    ]