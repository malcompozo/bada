from django.db import models
import random


############################### EVENT BOOKING ###############################

class EventBooking(models.Model):
    search_id = models.CharField(max_length=100, default=random.randint(0, 281474976710655), editable=False, verbose_name='ID de busqueda') 
    state = models.CharField(max_length=100,null=True, blank=True, verbose_name="Estado")
    booking_date = models.CharField(max_length=30, null=True, blank=True, verbose_name="fecha de reserva")
    site = models.CharField(max_length=50, null=True, blank=True, verbose_name="Recinto")
    banquetry = models.CharField(max_length=50, null=True, blank=True, verbose_name="Banqueteria")
    animation = models.CharField(max_length=50, null=True, blank=True, verbose_name="Animación")
    event_type = models.CharField(max_length=50, null=True, blank=True, verbose_name="Tipo de evento")
    capacity = models.PositiveIntegerField(default=50, null=True, blank=True, verbose_name="Capacidad")
    ilumination = models.CharField(max_length=50, null=True, blank=True, verbose_name="Iluminación")
    photographer = models.CharField(max_length=50, null=True, blank=True, verbose_name="Fotógrafo")
    value = models.PositiveIntegerField(default=350000, null=True, blank=True, verbose_name="Total a pagar")

    created = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Ultima edición")
    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"
        ordering = ['-created']

    def __str__(self):
        return self.event_type     


############################### CUSTOMERS ###############################
class Customer(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    last_name = models.CharField(max_length=100, verbose_name="Apellido")
    email = models.EmailField(max_length=100, verbose_name="Correo electrónico")
    rut = models.CharField(max_length=100, verbose_name="Rut")
    phone = models.CharField(max_length=100, verbose_name="Teléfono")
    address = models.CharField(max_length=100, verbose_name="Dirección")
    city = models.CharField(max_length=100, verbose_name="Ciudad")
    event = models.ForeignKey(EventBooking, related_name="evento", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ['-created']

    def __str__(self):
        return self.name



