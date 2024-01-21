from django.shortcuts import render
import requests
import pandas as pd
import json
import math
import datetime
import time

# Create your views here.
def index(request):
    city = request.GET.get('city', 'ratlam')
    day = request.GET.get('day', 13)
    month = request.GET.get('month', 4)
    year = request.GET.get('year', 2023)
    mystr = str(year) + "-" + str(month) + "-" + str(day) 
    date_string = mystr  # converted int to str
    date_object = datetime.datetime.strptime(date_string, "%Y-%m-%d")
    timestamp = date_object.timestamp() 
    unix_timestamp = int(timestamp)
    # print(unix_timestamp)
    # city='ratlam'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=594687f3ed4f53cf718a89e639dea2f5&dt={unix_timestamp}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        # print(data)
        timestamp = data['dt']
        dt = datetime.datetime.fromtimestamp(timestamp)
        human_date = dt.strftime('%Y-%m-%d')
        #  print(human_date)
        my_dict = {
            'city': data['name'],
            'weather': data['weather'][0]['main'],
            'icon': data['weather'][0]['icon'], 
            # default temp in kelvin, convert k to c and k to f 
            # 'temp' == 'kelvin'
            'c_temp': math.floor(data['main']['temp']-273),
            # 'f_temp': math.floor(data['main']['temp']),
            'f_temp': math.floor((9/5)*(math.floor(data['main']['temp']-273))+32),
             
            'feels_like': math.floor(data['main']['feels_like']-273),
            'humidity': data['main']['humidity'],              
            'pressure': data['main']['pressure'],
            'wind': data['wind']['speed'],
            'date':human_date,
            } 
        context = {'my_weather': my_dict}
        # print(context)
    else:
        print('Error:', response.status_code) 
    return render(request,"Weather/index.html",context)