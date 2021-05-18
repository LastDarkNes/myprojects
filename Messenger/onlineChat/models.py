from django.db import models

class Messedge(models.Model):
    author = models.CharField(max_length=50, null = True)
    text = models.TextField(null = True, verbose_name='Описание')
    date = models.DateTimeField(auto_now=True)
