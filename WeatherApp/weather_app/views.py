from django.shortcuts import render

def index(request):
    return render(request, 'weather_app/index.html')

def info(request):
    return render(request, 'weather_app/info.html')

