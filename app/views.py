from django.shortcuts import render

# Create your views here.

def wish(request):
    d={'name':'Bindu Sagar'}
    return render(request,'wish.html',d)

def conditions(request):
    d={'a':20,'b':30, 'c':40}
    return render(request,'conditions.html',d)

def loop(request):
    d={'name':'Madhu'}
    return render(request,'loop.html',d)
