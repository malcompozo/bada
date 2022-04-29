from django.db import models
from django.forms import ImageField

class Slider(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=200)
    content = models.CharField(max_length=200)
    image = models.ImageField(verbose_name='Foto de perfil', upload_to = 'slider')

    class Meta:
        verbose_name = "Slider de fotos"
        verbose_name_plural = "Slider de fotos"

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.CharField(max_length=250)

    class Meta:
        verbose_name = "Contacto"
        verbose_name_plural = "Contacto"

    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField(max_length=50)
    salon = models.CharField(max_length=50)
    capacity = models.IntegerField(default=50)
    description = models.TextField(max_length=500)

    class Meta:
        verbose_name = "Consultar evento"
        verbose_name_plural = "Consultar evento"

    def __str__(self):
        return self.title