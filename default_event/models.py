from django.db import models

# Create your models here.
##################################  EVENTOS PREDEFINIDOS #################################

class Site(models.Model):
    items = models.CharField(max_length=100, verbose_name="Recinto")
    urlBase = models.URLField(max_length=500, verbose_name="URL de la imagen")
    address = models.CharField(max_length=200, verbose_name="Dirección")
    capacity = models.PositiveIntegerField(verbose_name="Capacidad")
    value = models.PositiveIntegerField(verbose_name="Valor")

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
    value = models.PositiveIntegerField(verbose_name="Valor")

    class Meta:
            verbose_name = "Musica"
            verbose_name_plural = "Musica"

    def __str__(self):
        return self.items

################ EVENTO PREDEFINIDO ################
class EventType(models.Model):
    type = models.CharField(max_length=100, verbose_name="Tipo de evento")
    description = models.TextField(max_length=250 ,  verbose_name="Descripción")
    urlBase = models.URLField(max_length=500, verbose_name="URL de la imagen")
    site = models.ForeignKey(Site, verbose_name="Recinto", on_delete=models.CASCADE)
    music = models.ForeignKey(Music, verbose_name="Musica", on_delete=models.CASCADE, blank=True, null=True)
    value = models.PositiveIntegerField(verbose_name="Valor")
    class Meta:
        verbose_name = "Evento predefinido"
        verbose_name_plural = "Eventos predefinidos"

    def __str__(self):
        return self.type

class Catering(models.Model):
    items = models.CharField(max_length=100, verbose_name="Comida")
    urlBase = models.URLField(max_length=500, verbose_name="URL de la imagen")
    description = models.CharField(max_length=100, verbose_name="Entrada")
    description2 = models.CharField(max_length=100, verbose_name="Fondo", blank=True, null=True)
    description3 = models.CharField(max_length=100, verbose_name="Postre", blank=True, null=True)
    value = models.PositiveIntegerField(verbose_name="Valor")
    eventType = models.ForeignKey(EventType, related_name="event_catering", on_delete=models.CASCADE)

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
    value = models.PositiveIntegerField(verbose_name="Valor")
    eventType = models.ForeignKey(EventType, related_name="event_drinks", on_delete=models.CASCADE)
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
    value = models.PositiveIntegerField(verbose_name="Valor")
    eventType = models.ForeignKey(EventType, related_name="event_entertainment", on_delete=models.CASCADE)
    class Meta:
            verbose_name = "Entretenimiento"
            verbose_name_plural = "Entretenimiento"

    def __str__(self):
        return self.items
