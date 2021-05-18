from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Messedge

def onlineChat(request):
    Messedges = Messedge.objects.all()


    if request.method == 'POST':

        name = request.POST['name']
        msgtext = request.POST['msgtext']
        new = Messedge(author = name, text = msgtext)
        new.save()

        return HttpResponseRedirect('/')

    return render(request, "onlineChat/Chat.html", {"Messedges" : Messedges})
