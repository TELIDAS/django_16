from django.db import models


class Plants(models.Model):
    link = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="")


class Dorama(models.Model):
    link = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="")
