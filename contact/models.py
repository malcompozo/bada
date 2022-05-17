from django.db import models


############################### CONTACT ###############################
class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    email = models.EmailField(max_length=100, verbose_name='Email')
    message = models.CharField(max_length=250, verbose_name='Mensaje')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')

    class Meta:
        verbose_name = "Contacto"
        verbose_name_plural = "Contacto"
        ordering = ['-created']

    def __str__(self):
        return self.name