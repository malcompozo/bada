from django.db import models

# Create your models here.
class Slider(models.Model):
    title = models.CharField(max_length=200, verbose_name='Titulo')
    description = models.TextField(verbose_name='Descripción')
    urlBase = models.CharField(verbose_name='API', max_length=200, default='https://badaeventos.herokuapp.com', editable=False)
    image = models.ImageField(upload_to='slider/images', verbose_name='Imagen')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Slider"
        verbose_name_plural = "Slider"

    def __str__(self):
        return self.title

