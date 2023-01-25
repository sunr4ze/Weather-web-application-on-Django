from django.shortcuts import render
import requests

def index(request):
    appid = '431b68bea085d48610d7d1eade1b7771'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid
    city = ''

    tmp_request = request
    tmp_request = str(tmp_request)
    tmp_request = tmp_request[26:]

    index = 0
    while tmp_request[index] != '&':
        city += tmp_request[index]
        index += 1

    res = requests.get(url.format(city)).json()
    print(res)

    return render(request, 'weather_app/index.html')

def info(request):
    return render(request, 'weather_app/info.html')

