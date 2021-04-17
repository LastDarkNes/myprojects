from django.shortcuts import render
from .models import New

# Create your views here.
def newsRender(request):

    news = New.objects.all()

    return render(request, "newsboard/newtemplate.html", {"news" : news})
