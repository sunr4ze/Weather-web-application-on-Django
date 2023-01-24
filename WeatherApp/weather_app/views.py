from django.shortcuts import render
import requests

def index(request):
    appid = '431b68bea085d48610d7d1eade1b7771'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid='+ appid
    city = 'Minsk'
    return render(request, 'weather_app/index.html')

def info(request):
    return render(request, 'weather_app/info.html')

