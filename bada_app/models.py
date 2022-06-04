from django.db import models
import uuid

def rawID():
    return uuid.uuid4
############################### EVENT BOOKING ############################### 

class EventBooking(models.Model):
    search_id = models.UUIDField(primary_key=True, default=rawID(), max_length=100, editable=False, verbose_name='ID de busqueda') 
    state = models.CharField(max_length=100, verbose_name="Estado")
    booking_date = models.CharField(max_length=30, verbose_name="fecha de reserva")
    event_type = models.CharField(max_length=50, verbose_name="Tipo de evento")
    description = models.TextField(max_length=250, verbose_name="Descripción")
    urlBase = models.URLField(max_length=500, verbose_name="URL de la imagen")
    people = models.PositiveIntegerField(verbose_name="Invitados")
    site = models.CharField(max_length=100, verbose_name="Sitio")
    music = models.CharField(max_length=100, verbose_name="Música")
    catering = models.CharField(max_length=100, verbose_name="Banqueteria")
    drinks = models.CharField(max_length=100, verbose_name="Bebidas")
    entertainment = models.CharField(max_length=100, verbose_name="Entretenimiento")
    value = models.PositiveIntegerField(verbose_name="Total a pagar")

    created = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Ultima edición")
    class Meta:
        verbose_name = "Evento reservado"
        verbose_name_plural = "Eventos reservados"
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
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    event_booking = models.ForeignKey(EventBooking, verbose_name="Eventos reservados", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ['-created']

    def __str__(self):
        return self.name




