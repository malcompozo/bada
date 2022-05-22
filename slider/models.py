from django.db import models

# Create your models here.
class Slider(models.Model):
    title = models.CharField(max_length=200, verbose_name='Titulo')
    description = models.TextField(verbose_name='Descripción')
    urlBase = models.URLField(max_length=500, verbose_name="URL de la imagen")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Slider"
        verbose_name_plural = "Slider"

    def __str__(self):
        return self.title

