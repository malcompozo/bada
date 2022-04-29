from django.db import models
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