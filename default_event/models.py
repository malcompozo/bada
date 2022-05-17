from django.db import models

# Create your models here.
##################################  EVENTOS PREDEFINIDOS #################################
class Group(models.Model):
    items = models.CharField(max_length=100, verbose_name="Tipo de publico")

    class Meta:
        verbose_name = "Tipo de publico"
        verbose_name_plural = "Tipo de publico"
    
    def __str__(self):
        return self.items

class Banquetry(models.Model):
    items = models.CharField(max_length=100, verbose_name="Item")
    value = models.PositiveIntegerField(verbose_name="Valor")

    class Meta:
        verbose_name = "Banqueteria"
        verbose_name_plural = "Banqueteria"
    
    def __str__(self):
        return self.items

class Site(models.Model):
    site = models.CharField(max_length=100, verbose_name="Recinto")
    adress = models.CharField(max_length=200, verbose_name="Dirección")
    capacity = models.PositiveIntegerField(verbose_name="Capacidad")
    value = models.PositiveIntegerField(verbose_name="Valor")

    class Meta:
        verbose_name = "Recinto"
        verbose_name_plural = "Recinto"

    def __str__(self):
        return self.site

class Music(models.Model):
    items = models.CharField(max_length=100,verbose_name="Musica")
    value = models.PositiveIntegerField(verbose_name="Valor")

    class Meta:
            verbose_name = "Musica"
            verbose_name_plural = "Musica"

    def __str__(self):
        return self.items

class Toys(models.Model):
    items = models.CharField(max_length=100, verbose_name="Juegos")
    value = models.PositiveIntegerField(verbose_name="Valor")
    class Meta:
            verbose_name = "Juegos"
            verbose_name_plural = "Juegos"

    def __str__(self):
        return self.items

################ EVENTO PREDEFINIDO ################
class EventTipe(models.Model):
    name = models.CharField(max_length=100, verbose_name="Tipo de evento")
    group = models.ForeignKey(Group, verbose_name="Tipo de publico", on_delete=models.CASCADE, blank=True, null=True)
    banquetry = models.ForeignKey(Banquetry, verbose_name="Banqueteria", on_delete=models.CASCADE)
    site = models.ForeignKey(Site, verbose_name="Recinto", on_delete=models.CASCADE)
    music = models.ForeignKey(Music, verbose_name="Musica", on_delete=models.CASCADE)
    toys = models.ForeignKey(Toys, verbose_name="Juegos", on_delete=models.CASCADE, blank=True, null=True)
    
    class Meta:
        verbose_name = "Evento predefinido"
        verbose_name_plural = "Eventos predefinidos"

    def __str__(self):
        return self.name
