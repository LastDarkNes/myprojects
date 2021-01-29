
from django.urls import path
from django.conf.urls import include
from newsboard import views

urlpatterns = [
    path('', views.newsRender),
]
