import requests
import pandas as pd
import json
city='indore'
url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=594687f3ed4f53cf718a89e639dea2f5'
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print('Error:', response.status_code)
# import requests
# import json
# city = "ratlam"
# url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=594687f3ed4f53cf718a89e639dea2f5'
# data = requests.get(url).json()
# print(data.response)