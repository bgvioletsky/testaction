import requests
from datetime import datetime
def getWeather(local):
    url = 'https://api.codelife.cc/api/weather/city?lang=cn&location='+local
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
        'Authorization': 'Token eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2MjExZWExOThmODk3ZDNhZGZiMWM3NTMiLCJpYXQiOjE3MDU5MDI3OTQsImV4cCI6MTczNzAwNjc5NH0.CjKNQfnjHQ3pofI94wkKuLHiyB_EeVFpQ6BhpC8QKY4',
        'Signaturekey': 'U2FsdGVkX19fsjh/WEtSmaTFRMkg3D94ZyAS4wwFazI='
    }
    response = requests.get(url, headers=headers).json()
    id=response['data'][0]['id']
    url1='https://api.codelife.cc/api/getWeather?lang=cn&location='+id
    response = requests.get(url1, headers=headers)
    list1=[
    "舒适度指数",
    "穿衣指数",
    "感冒指数",
    "运动指数",
    "旅游指数",
    "紫外线指数",
    "洗车指数",
    "钓鱼指数"
]
    if response.status_code == 200:
        data = response.json()
        text="渠县天气\n温度 : "+data['data']['now']['tmp']+"°      气压 : "+data['data']['now']['pres']+"hPa      天气 : "+data['data']['now']['cond_txt']+"\n风向 : "+data['data']['now']['wind_dir']+"    湿度 : "+data['data']['now']['hum']+"%"
        shenhuo=data['data']['lifestyle']
        x=0
        for i in shenhuo:
          if x % 3 == 0:
                text=text+"\n"+ list1[x]+" : "+ i['brf']+"    "
          else:
                 text=text+ list1[x]+" : "+ i['brf']+"    "
          
          x=x+1
       
    else:
        print('Failed to fetch data.')
    print(text)
    return text
