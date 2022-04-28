from django.db import models

class Slider(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=100)
    image = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField(max_length=50)
    salon = models.CharField(max_length=50)
    capacity = models.IntegerField(default=50)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.title