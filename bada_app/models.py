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

class EstadoEvento(models.Model):
    estado = models.CharField(max_length=100)
    fecha = models.DateTimeField(auto_now_add=True)
    recinto = models.CharField(max_length=50)
    banqueteria = models.CharField(max_length=50)
    animacion = models.CharField(max_length=50)
    tipo_evento = models.CharField(max_length=50)
    capacity = models.IntegerField(default=50)
    iluminacion = models.CharField(max_length=50)
    fotografo = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Consultar evento"
        verbose_name_plural = "Consultar evento"

    def __str__(self):
        return self.tipo_evento