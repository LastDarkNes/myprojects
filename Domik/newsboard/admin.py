from django.contrib import admin
from .models import New, Category

class NewAdmin(admin.ModelAdmin):
    list_display = ['category', ...]

admin.site.register(New)
admin.site.register(Category)
