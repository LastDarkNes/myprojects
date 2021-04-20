from django.shortcuts import render
from .models import Messedge
# Create your views here.
def onlineChat(request):
    Messedges = Messedge.objects.all()
    if 'q' in request.POST:
            q = request.POST['q']
            return render_to_response('index.html', {'q': q} )
    else:

        return render(request, "onlineChat/Chat.html", {"Messedges" : Messedges})
