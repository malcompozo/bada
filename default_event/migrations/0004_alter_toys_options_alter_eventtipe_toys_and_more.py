# Generated by Django 4.0.3 on 2022-05-17 03:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('default_event', '0003_alter_eventtipe_banquetry_alter_eventtipe_group_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='toys',
            options={'verbose_name': 'Entretenimiento', 'verbose_name_plural': 'Entretenimiento'},
        ),
        migrations.AlterField(
            model_name='eventtipe',
            name='toys',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='default_event.toys', verbose_name='Entretenimiento'),
        ),
        migrations.AlterField(
            model_name='toys',
            name='items',
            field=models.CharField(max_length=100, verbose_name='Entretenimiento'),
        ),
    ]
