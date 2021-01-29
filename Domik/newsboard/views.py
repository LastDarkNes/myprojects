from django.shortcuts import render
from .models import New

# Create your views here.
def newsRender(request):
    News = New.objects.all()
    return render(request, "index.html", {"News" : News})
