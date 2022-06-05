from django.db import models


class Plants(models.Model):
    class Meta:
        verbose_name = "Искусственное растение"
        verbose_name_plural = "Искусственные Растения"
    link = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="")


class Dorama(models.Model):
    class Meta:
        verbose_name = "Дорама"
        verbose_name_plural = "Дорамалар"
    link = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="")
