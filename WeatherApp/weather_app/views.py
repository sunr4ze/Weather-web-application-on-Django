from django.shortcuts import render

def index(request):
    return render(request, 'weather_app/index.html')

def about(request):
    return render(request, 'weather_app/about.html')

def contacts(request):
    return render(request, 'weather_app/contacts.html')

def maps(request):
    return render(request, 'weather_app/maps.html')
