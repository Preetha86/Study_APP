from django.shortcuts import render

def First(request):
    return render(request,'First.html')

def Second(request):
    return render(request,'Second.html')