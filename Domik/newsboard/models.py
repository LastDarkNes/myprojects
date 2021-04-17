from django.db import models



class Category(models.Model):
    def __str__ (self):
        return self.name

    name = models.CharField(max_length=64, verbose_name='название')

class New(models.Model):
    def __str__ (self):
        return self.title

    title = models.CharField(max_length=30, verbose_name='Заголовок')
    description = models.TextField(null = True, verbose_name='Описание')
    image = models.ImageField(upload_to='', null=True, blank=True, verbose_name='Изображение')
    date = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория', null=True)
