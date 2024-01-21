from django.shortcuts import render
import requests
import json
import pandas as pd
from sqlalchemy import create_engine
import numpy as np
# Create your views here.
def corona(request):
    url = f'https://coronavirus.m.pipedream.net/'
    response = requests.get(url)
    if response.status_code == 200:
        conn = create_connection()
        data = response.json()
        # if len(data['rawData']) > 0:
        df = pd.DataFrame(data['rawData'])
        df.rename(
            columns={
                'Province_State': 'ProvinceState',
                'Country_Region': 'CountryRegion',
                'Last_Update': 'LastUpdated',
                'Long_': 'Long',
                'Case_Fatality_Ratio': 'CaseFatalityRate'
                },
            inplace=True)
        
        df = df.drop(['FIPS', 'Admin2', 'Recovered', 'Incident_Rate', 'Combined_Key', 'Active'], axis=1)
       
        df['ProvinceState'] = df['ProvinceState'].fillna(0.0)
        df['CountryRegion'] = df['CountryRegion'].fillna(0.0)
        df['LastUpdated'] = df['LastUpdated'].fillna(0.0)
        
        df['Lat'] = df['Lat'].fillna(0.0)
        df['Long'] = df['Long'].fillna(0.0)
        df['Confirmed'] = df['Confirmed'].fillna(0.0)
        df['Deaths'] = df['Deaths'].fillna(0.0)
        df['CaseFatalityRate'] = df['CaseFatalityRate'].fillna(0.0)
        print(df)
        import pdb; pdb.set_trace()
        df.to_sql('coronadata', con=conn, schema='corona', if_exists='append', index=False)
        # query = """INSERT INTO corona.coronadata(ProvinceState, CountryRegion, Lat, Long, 
        # Confirmed, Deaths, CaseFatalityRate, LastUpdate)VALUES(%s, %s, %s, %s,%s,%s,%s,%s)"""
        corona_data = {
            'alldata':data['rawData']
        }
     

    else:
        print("error")
    return render(request, "eventapp/corona.html", {'corona_data':corona_data})

def create_connection():
    try:
        engine = create_engine('postgresql://postgres:12345@localhost:5432/postgres')
        return engine
    except:
        print("Unable to create connection...")
        
    return None

# def corona(request):
#     url = f'https://coronavirus.m.pipedream.net/'
#     response = requests.get(url)
#     if response.status_code == 200:
#         data = response.json()
#         print(data)
#         corona_data ={
#             'alldata':data['rawData']
#         }
#     else:
#         print("error")
#     return render(request,"eventapp/corona.html",{'corona_data':corona_data})
      