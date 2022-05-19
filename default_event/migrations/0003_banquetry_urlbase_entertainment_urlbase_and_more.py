# Generated by Django 4.0.3 on 2022-05-19 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('default_event', '0002_rename_items_group_ages_rename_adress_site_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='banquetry',
            name='urlBase',
            field=models.CharField(default='https://badaeventos.herokuapp.com', editable=False, max_length=200, verbose_name='API'),
        ),
        migrations.AddField(
            model_name='entertainment',
            name='urlBase',
            field=models.CharField(default='https://badaeventos.herokuapp.com', editable=False, max_length=200, verbose_name='API'),
        ),
        migrations.AddField(
            model_name='eventtipe',
            name='urlBase',
            field=models.CharField(default='https://badaeventos.herokuapp.com', editable=False, max_length=200, verbose_name='API'),
        ),
        migrations.AddField(
            model_name='music',
            name='urlBase',
            field=models.CharField(default='https://badaeventos.herokuapp.com', editable=False, max_length=200, verbose_name='API'),
        ),
        migrations.AddField(
            model_name='site',
            name='urlBase',
            field=models.CharField(default='https://badaeventos.herokuapp.com', editable=False, max_length=200, verbose_name='API'),
        ),
    ]
