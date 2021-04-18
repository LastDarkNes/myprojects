from django.shortcuts import render


# Create your views here.
def Reg(request):
    return render(request, 'registration/regtemplate.html')
