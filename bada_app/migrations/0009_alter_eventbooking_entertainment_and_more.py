# Generated by Django 4.0.3 on 2022-05-18 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bada_app', '0008_rename_photographer_eventbooking_entertainment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventbooking',
            name='entertainment',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Entretenimiento'),
        ),
        migrations.AlterField(
            model_name='eventbooking',
            name='group',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Tipo de publico'),
        ),
        migrations.AlterField(
            model_name='eventbooking',
            name='search_id',
            field=models.CharField(default=54873720824067, editable=False, max_length=100, verbose_name='ID de busqueda'),
        ),
    ]
