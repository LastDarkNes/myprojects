from django.db import models

class New(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(null = True,max_length=30)
    image = models.ImageField(upload_to='static', blank=True)
