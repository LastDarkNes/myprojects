from django.db import models

class New(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(null = True)
    image = models.ImageField(upload_to='', null=True, blank=True)
    date = models.DateTimeField(auto_now=True)
