import json

import requests
import datetime
import json
import pandas as pd

INP_DATE = (datetime.datetime.today() + datetime.timedelta(days= 1)).strftime("%d-%m-%Y")
PIN = 440009
DIST_ID = 365

data_vac = []
columns_vac = ['center_name', 'pincode', 'date', 'available_capacity', 'vaccine', 'min_age_limit']
URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={}&date={}".format(
        DIST_ID, INP_DATE)
response = requests.get(URL)
print(response.json())
'''
rep = response.json()
for i in rep['centers']:
    # print(i['name'],'\t',i['lat'],i['long'])
    for j in i['sessions']:
        # if j['min_age_limit'] == 18 and j['available_capacity'] > 0 :
            value = [i['name'], i['pincode'], j['date'], j['available_capacity'], j['vaccine'], j['min_age_limit']]
            data_vac.append(value)
        # print(value)
df = pd.DataFrame(data_vac, columns=columns_vac)
print(df)
'''