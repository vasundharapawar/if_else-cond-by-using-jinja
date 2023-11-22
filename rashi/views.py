from django.shortcuts import render

# Create your views here.

def con_fun(request):
    d = {'a':10,'b':20,'c':15}
    return render(request,'rashi.html',d)