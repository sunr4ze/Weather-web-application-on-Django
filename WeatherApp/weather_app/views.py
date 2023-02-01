from django.shortcuts import render
import requests
from . import city_ident
from .forms import CityForm

def index(request):
    appid = '431b68bea085d48610d7d1eade1b7771'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid
    city = city_ident.city_ident(request)
    print(city)
    res = requests.get(url.format(city)).json()
    print(res)
    if request.method=='POST':
        form = CityForm(request.POST)
        form.save()
        city_info = {
            'city': city,
            'temp': res["main"]["temp"],
            'icon': res["weather"][0]["icon"],
            'wind': res["wind"]["speed"],
            'humidity': res["main"]["humidity"],
            'clouds': res["clouds"]["all"]
        }
        form = CityForm()
        context = {'info': city_info, 'form': form}
        return render(request, 'weather_app/index.html', context)
    else:
        city = 'Minsk'
        res = requests.get(url.format(city)).json()
        city_info = {
            'city': city,
            'temp': res["main"]["temp"],
            'icon': res["weather"][0]["icon"],
            'wind': res["wind"]["speed"],
            'humidity': res["main"]["humidity"],
            'clouds': res["clouds"]["all"]
        }

        context = {'info': city_info}
        return render(request, 'weather_app/index.html', context)


def info(request):
    return render(request, 'weather_app/info.html')

