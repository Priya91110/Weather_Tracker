import psycopg2, json, requests
import requests
import pandas as pd

# conn =psycopg2.connect(dbname="postgres", user="postgres",password="12345",host="localhost", port="5432")

url='https://coronavirus.m.pipedream.net/'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    # print(data)
    df = pd.DataFrame(data['rawData'])
    print(df.head(5))
else:
    print('Failed to retrieve global COVID-19 data.')


# # import psycopg2
# # import os
# # conn = psycopg2.connect(dbname="postgres",user="postgres",password="12345",host="localhost",port="5432")
# # print("Connection to database successful!")
# # with open("first_csv.csv", 'r') as csvfile:
# #     cursor = conn.cursor()
# #     cursor.execute('''select *from apis.state;''')
# #     print(cursor.fetchall()) 
# #     cursor.copy_expert("COPY apis.state('state-province','name','country','web_pages','domains','alpha_two_code');",csvfile)
# #     conn.commit()    


