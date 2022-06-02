from django.db import models
import uuid

def rawID():
    return uuid.uuid4
############################### EVENT BOOKING ############################### 

class Site(models.Model):
    items = models.CharField(max_length=100, verbose_name="Recinto")
    urlBase = models.URLField(max_length=500, verbose_name="URL de la imagen")
    address = models.CharField(max_length=200, verbose_name="Dirección")

    class Meta:
        verbose_name = "Recinto"
        verbose_name_plural = "Recinto"

    def __str__(self):
        return self.items

class Music(models.Model):
    items = models.CharField(max_length=100,verbose_name="Musica")
    urlBase = models.URLField(max_length=500, verbose_name="URL de la imagen")
    description = models.CharField(max_length=100, verbose_name="Descripción")
    description2 = models.CharField(max_length=100, verbose_name="Descripción2", blank=True, null=True)

    class Meta:
            verbose_name = "Musica"
            verbose_name_plural = "Musica"

    def __str__(self):
        return self.items

class Catering(models.Model):
    items = models.CharField(max_length=100, verbose_name="Comida")
    urlBase = models.URLField(max_length=500, verbose_name="URL de la imagen")
    description = models.CharField(max_length=100, verbose_name="Entrada")
    description2 = models.CharField(max_length=100, verbose_name="Fondo", blank=True, null=True)
    description3 = models.CharField(max_length=100, verbose_name="Postre", blank=True, null=True)

    class Meta:
        verbose_name = "Banqueteria"
        verbose_name_plural = "Banqueteria"
    
    def __str__(self):
        return self.items

class Drinks(models.Model):
    items = models.CharField(max_length=100, verbose_name="Bebestible")
    urlBase = models.URLField(max_length=500, verbose_name="URL de la imagen")
    description = models.CharField(max_length=100, verbose_name="Descripción")
    description2 = models.CharField(max_length=100, verbose_name="Descripción2", blank=True, null=True)
    class Meta:
            verbose_name = "Bebestible"
            verbose_name_plural = "Bebestibles"

    def __str__(self):
        return self.items

class Entertainment(models.Model):
    items = models.CharField(max_length=100, verbose_name="Entretenimiento")
    urlBase = models.URLField(max_length=500, verbose_name="URL de la imagen")
    description = models.CharField(max_length=100, verbose_name="Descripción")
    description2 = models.CharField(max_length=100, verbose_name="Descripción2", blank=True, null=True)
    class Meta:
            verbose_name = "Entretenimiento"
            verbose_name_plural = "Entretenimiento"

    def __str__(self):
        return self.items

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

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ['-created']

    def __str__(self):
        return self.name

################ EVENTO PREDEFINIDO ################
class EventBooking(models.Model):
    search_id = models.UUIDField(primary_key=True, default=rawID(), max_length=100, editable=False, verbose_name='ID de busqueda') 
    state = models.CharField(max_length=100, verbose_name="Estado", null=True, blank=True)
    booking_date = models.CharField(max_length=30, verbose_name="fecha de reserva")
    event_type = models.CharField(max_length=50, verbose_name="Tipo de evento")
    description = models.TextField(max_length=250, verbose_name="Descripción")
    urlBase = models.URLField(max_length=500, verbose_name="URL de la imagen")
    people = models.PositiveIntegerField(verbose_name="Invitados")
    ##### FOREIGN KEY #####
    site = models.ForeignKey(Site, verbose_name="Recinto", on_delete=models.CASCADE)
    music = models.ForeignKey(Music, verbose_name="Musica", on_delete=models.CASCADE)
    catering = models.ForeignKey(Catering, verbose_name="Comida", on_delete=models.CASCADE)
    drinks = models.ForeignKey(Drinks, verbose_name="Bebestible", on_delete=models.CASCADE)
    entertainment = models.ForeignKey(Entertainment, verbose_name="Entretenimiento", on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, verbose_name="Cliente", on_delete=models.CASCADE, blank=True, null=True)
    value = models.PositiveIntegerField(verbose_name="Total a pagar")

    created = models.DateTimeField(auto_now_add=True, verbose_name="fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Ultima edición")
    class Meta:
        verbose_name = "Evento reservado"
        verbose_name_plural = "Eventos reservados"
        ordering = ['-created']

    def __str__(self):
        return self.event_type   
  

class Imagen(models.Model):
    imagen = models.ImageField(upload_to='imagenes', verbose_name="Imagen")

    class Meta:
        verbose_name = "Imagen"
        verbose_name_plural = "Imagenes"

    def __str__(self):
        return self.imagen.url




