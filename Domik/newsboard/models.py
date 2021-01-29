from django.db import models

class New(models.Model):
    title = models.CharField(max_length=30)
    text = models.TextField(null = True)
