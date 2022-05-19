from django.db import models

# Create your models here.
##################################  EVENTOS PREDEFINIDOS #################################
class Group(models.Model):
    ages = models.CharField(max_length=100, verbose_name="Tipo de publico")

    class Meta:
        verbose_name = "Tipo de publico"
        verbose_name_plural = "Tipo de publico"
    
    def __str__(self):
        return self.items

class Banquetry(models.Model):
    items = models.CharField(max_length=100, verbose_name="Item")
    urlBase = models.CharField(verbose_name='API', max_length=200, default='https://badaeventos.herokuapp.com', editable=False)
    image = models.ImageField(upload_to='banquetry/images', verbose_name="Imagen")
    description = models.CharField(max_length=100, verbose_name="Descripción")
    description2 = models.CharField(max_length=100, verbose_name="Descripción2", blank=True, null=True)
    value = models.PositiveIntegerField(verbose_name="Valor")

    class Meta:
        verbose_name = "Banqueteria"
        verbose_name_plural = "Banqueteria"
    
    def __str__(self):
        return self.items

class Site(models.Model):
    site = models.CharField(max_length=100, verbose_name="Recinto")
    urlBase = models.CharField(verbose_name='API', max_length=200, default='https://badaeventos.herokuapp.com', editable=False)
    image = models.ImageField(upload_to='site/images', verbose_name="Imagen")
    address = models.CharField(max_length=200, verbose_name="Dirección")
    capacity = models.PositiveIntegerField(verbose_name="Capacidad")
    value = models.PositiveIntegerField(verbose_name="Valor")

    class Meta:
        verbose_name = "Recinto"
        verbose_name_plural = "Recinto"

    def __str__(self):
        return self.site

class Music(models.Model):
    items = models.CharField(max_length=100,verbose_name="Musica")
    urlBase = models.CharField(verbose_name='API', max_length=200, default='https://badaeventos.herokuapp.com', editable=False)
    image = models.ImageField(upload_to='music/images', verbose_name="Imagen")
    description = models.CharField(max_length=100, verbose_name="Descripción")
    description2 = models.CharField(max_length=100, verbose_name="Descripción2", blank=True, null=True)
    value = models.PositiveIntegerField(verbose_name="Valor")

    class Meta:
            verbose_name = "Musica"
            verbose_name_plural = "Musica"

    def __str__(self):
        return self.items

class Entertainment(models.Model):
    items = models.CharField(max_length=100, verbose_name="Entretenimiento")
    urlBase = models.CharField(verbose_name='API', max_length=200, default='https://badaeventos.herokuapp.com', editable=False)
    image = models.ImageField(upload_to='entertainment/images', verbose_name="Imagen")
    description = models.CharField(max_length=100, verbose_name="Descripción")
    description2 = models.CharField(max_length=100, verbose_name="Descripción2", blank=True, null=True)
    value = models.PositiveIntegerField(verbose_name="Valor")
    class Meta:
            verbose_name = "Entretenimiento"
            verbose_name_plural = "Entretenimiento"

    def __str__(self):
        return self.items

################ EVENTO PREDEFINIDO ################
class EventTipe(models.Model):
    name = models.CharField(max_length=100, verbose_name="Tipo de evento")
    urlBase = models.CharField(verbose_name='API', max_length=200, default='https://badaeventos.herokuapp.com', editable=False)
    image = models.ImageField(upload_to='event_tipe/images', verbose_name="Imagen")
    group = models.ForeignKey(Group, verbose_name="Tipo de publico", on_delete=models.CASCADE, blank=True, null=True)
    banquetry = models.ForeignKey(Banquetry, verbose_name="Banqueteria", on_delete=models.CASCADE, blank=True, null=True)
    site = models.ForeignKey(Site, verbose_name="Recinto", on_delete=models.CASCADE)
    music = models.ForeignKey(Music, verbose_name="Musica", on_delete=models.CASCADE, blank=True, null=True)
    entertainment = models.ForeignKey(Entertainment, verbose_name="Entretenimiento", on_delete=models.CASCADE, blank=True, null=True)
    
    class Meta:
        verbose_name = "Evento predefinido"
        verbose_name_plural = "Eventos predefinidos"

    def __str__(self):
        return self.name
