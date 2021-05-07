from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import requests
import datetime
import json
import pandas as pd

INP_DATE = (datetime.datetime.today() + datetime.timedelta(days= 1)).strftime("%d-%m-%Y")
PIN = 440009
DIST_ID = 365
district = 'Nagpur'
def hi(request):
    print(request.GET)
    district = request.GET.get('district')
    if district == 'Mumbai':
        DIST_ID = 395
    elif district == 'Bangalore':
        DIST_ID = 265
    else :
        DIST_ID = 365
    data_vac = []
    columns_vac = ['center_name', 'pincode', 'date', 'available_capacity', 'vaccine', 'min_age_limit']
    URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={}&date={}".format( DIST_ID, INP_DATE)
    response = requests.get(URL)
    rep = response.json()
    for i in rep['centers']:
        # print(i['name'],'\t',i['lat'],i['long'])
        for j in i['sessions']:
            # j['min_age_limit'] == 18 and
            if j['available_capacity'] > 0 :
                value = [i['name'], i['pincode'], j['date'], j['available_capacity'], j['vaccine'], j['min_age_limit']]
                data_vac.append(value)
        # print(value)
    df = pd.DataFrame(data_vac, columns=columns_vac)
    all_data = []
    for i in range(df.shape[0]):
        temp = df.iloc[i]
        all_data.append(dict(temp))

    context = {'data':all_data }
    return render(request,'demo_app/hi.html',context=context)
