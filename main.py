import json
import requests
import datetime
import time

opentime= int(7)*60+int(5)
closetime=int(23)*60 + int(5)
timenow=datetime.datetime.now().hour*60+datetime.datetime.now().minute

print(opentime)
print(closetime)
print(timenow)

PIN = '110001'

while(timenow>= opentime and timenow<=closetime):
  time.sleep(10)
  def get_list():

    time_response = requests.get('http://worldclockapi.com/api/json/utc/now')

    time_full = json.loads(time_response.text)
    #print(time['currentDateTime'])
    time = time_full['currentDateTime'][0:10]
    date_indian = time[8:10]+'-'+time[5:7]+'-'+time[0:4]


    url = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode='+PIN+'&date='+date_indian

    headers = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\ AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
      }

    response_json = requests.get(url,headers = headers)
    data = json.loads(response_json.text)
    return data


  data = get_list()

  centers = data['centers']




  for center in centers:
    found = 0
    center_name = center['name']
    sessions_list = center['sessions']

    for sessions in sessions_list:

      if(sessions['available_capacity'] >0 and sessions['min_age_limit']==18):
        print(f'SLOT FOUND for {center_name} at date '+ sessions['date']+'\n')
        found=1


    if(found==0):
      print(f'slot not found for center {center_name}')

