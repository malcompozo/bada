# Generated by Django 4.0.3 on 2022-06-02 01:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('default_event', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventtype',
            name='group',
        ),
        migrations.DeleteModel(
            name='Group',
        ),
    ]
