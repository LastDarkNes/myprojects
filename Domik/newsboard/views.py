from django.shortcuts import render
from .models import New

# Create your views here.
def newsRender(request):

    disc = New.objects.all()

    return render(request, "html/newtemplate.html", {"disc" : disc})
