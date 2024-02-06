import json
import requests
from datetime import datetime


def getWeather(local):
    now = datetime.now()
    formatted_date = now.strftime("%m-%d")
    time = now.strftime("%H:%M")
    date = now.date()  # 获取当前日期
    folder = str(date)
    # folder='2024-01-21'
    url = 'https://api.codelife.cc/api/weather/city?lang=cn&location=' + local
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
        'Authorization': 'Token eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2MjExZWExOThmODk3ZDNhZGZiMWM3NTMiLCJpYXQiOjE3MDU5MDI3OTQsImV4cCI6MTczNzAwNjc5NH0.CjKNQfnjHQ3pofI94wkKuLHiyB_EeVFpQ6BhpC8QKY4',
        'Signaturekey': 'U2FsdGVkX19fsjh/WEtSmaTFRMkg3D94ZyAS4wwFazI='
    }
    response = requests.get(url, headers=headers).json()['data'][0]['id']
    url1 = 'https://api.codelife.cc/api/getWeather?lang=cn&location=' + response
    response = requests.get(url1, headers=headers)
    if response.status_code == 200:
        data = response.json()['data']
        tmp = data['now']['tmp']
        pres = data['now']['pres']
        cond_txt = data['now']['cond_txt']
        wind_dir = data['now']['wind_dir']
        wind_sc = data['now']['wind_sc']
        hum = data['now']['hum']
        pcpn = data['now']['pcpn']
        lifestyle = data['lifestyle']
        qlty = data['air_now_city']['qlty']
        aqi = data['air_now_city']['aqi']
        comf = lifestyle[0]['brf']
        drsg = lifestyle[1]['brf']
        flu = lifestyle[2]['brf']
        trav = lifestyle[3]['brf']
        uv = lifestyle[4]['brf']
        cw = lifestyle[5]['brf']
        fsh = lifestyle[6]['brf']
        txt = data['rain']['txt']
        daily_forecast = data['daily_forecast'][0]
        tmp_min = daily_forecast['tmp_min']
        tmp_max = daily_forecast['tmp_max']
        ss = daily_forecast['ss']
        sr = daily_forecast['sr']
        fileurl = folder + '/img_name.json'
        with open(fileurl, 'r') as f:
            fileurls = json.load(f)
        imgurl = list(set(fileurls))
        variables = {
            'tmp': tmp,
            'pres': pres,
            'time': time,
            'formatted_date': formatted_date,
            'cond_txt': cond_txt,
            'wind_dir': wind_dir,
            'wind_sc': wind_sc,
            'hum': hum,
            'pcpn': pcpn,
            'qlty': qlty,
            'txt': txt,
            'aqi': aqi, 'comf': comf, 'drsg': drsg, 'flu': flu, 'trav': trav, 'uv': uv, 'fsh': fsh, 'cw': cw,
            'tmp_min': tmp_min, 'tmp_max': tmp_max, 'ss': ss, 'sr': sr,'imgurl[0]':imgurl[0],'imgurl[1]':imgurl[1],'imgurl[2]':imgurl[2],'imgurl[3]':imgurl[3],'imgurl[4]':imgurl[4],'imgurl[5]':imgurl[5],'imgurl[6]':imgurl[6],'imgurl[7]':imgurl[7],'imgurl[8]':imgurl[8],'imgurl[9]':imgurl[9],'imgurl[10]':imgurl[10],'imgurl[11]':imgurl[11],'imgurl[12]':imgurl[12],'imgurl[13]':imgurl[13],'imgurl[14]':imgurl[14],'imgurl[15]':imgurl[15],'imgurl[16]':imgurl[16],'imgurl[17]':imgurl[17],'imgurl[18]':imgurl[18],'imgurl[19]':imgurl[19]
        }

        with open('./test.html', 'r') as file:
            # 读取文件内容
            bg = file.read()
        for key, value in variables.items():
            bg = bg.replace('{' + key + '}', value)

    else:
        print('Failed to fetch data.')

    return bg


def write_text_to_file(text):
    with open('text.html', 'w') as f:
        f.write(text)


write_text_to_file(getWeather('渠县'))
# getWeather('渠县')
