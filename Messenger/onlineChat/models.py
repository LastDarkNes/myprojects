from django.db import models

class Messedge(models.Model):
    text = models.TextField(null = True, verbose_name='Описание')
    date = models.DateTimeField(auto_now=True)
