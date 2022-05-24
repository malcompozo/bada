# Generated by Django 4.0.3 on 2022-05-24 03:06

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EventBooking',
            fields=[
                ('search_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID de busqueda')),
                ('state', models.CharField(blank=True, max_length=100, null=True, verbose_name='Estado')),
                ('booking_date', models.CharField(blank=True, max_length=30, null=True, verbose_name='fecha de reserva')),
                ('site', models.CharField(blank=True, max_length=50, null=True, verbose_name='Recinto')),
                ('address', models.CharField(max_length=200, verbose_name='Dirección')),
                ('capacity', models.PositiveIntegerField(blank=True, default=50, null=True, verbose_name='Capacidad')),
                ('banquetry', models.CharField(blank=True, max_length=50, null=True, verbose_name='Banqueteria')),
                ('event_type', models.CharField(blank=True, max_length=50, null=True, verbose_name='Tipo de evento')),
                ('group', models.CharField(blank=True, max_length=50, null=True, verbose_name='Tipo de publico')),
                ('music', models.CharField(max_length=100, verbose_name='Musica')),
                ('entertainment', models.CharField(blank=True, max_length=50, null=True, verbose_name='Entretenimiento')),
                ('value', models.PositiveIntegerField(blank=True, null=True, verbose_name='Total a pagar')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Ultima edición')),
            ],
            options={
                'verbose_name': 'Evento reservado',
                'verbose_name_plural': 'Eventos reservados',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('last_name', models.CharField(max_length=100, verbose_name='Apellido')),
                ('email', models.EmailField(max_length=100, verbose_name='Correo electrónico')),
                ('rut', models.CharField(max_length=100, verbose_name='Rut')),
                ('phone', models.CharField(max_length=100, verbose_name='Teléfono')),
                ('address', models.CharField(max_length=100, verbose_name='Dirección')),
                ('city', models.CharField(max_length=100, verbose_name='Ciudad')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bada_app.eventbooking', verbose_name='Evento')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'ordering': ['-created'],
            },
        ),
    ]
