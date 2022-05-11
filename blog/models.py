from django.db import models



class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)