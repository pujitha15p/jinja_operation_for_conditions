from django.shortcuts import render

# Create your views here.

def conditions(request):
    d={'a':5100,'b':1000,'c':90000}


    return render(request,'conditions.html',d)