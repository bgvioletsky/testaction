import json
import requests
from datetime import datetime
def getWeather(local):
    now = datetime.now()
    formatted_date = now.strftime("%m-%d")
    time=now.strftime("%H:%M")
    date = now.date()  # 获取当前日期
    folder = str(date)
    # folder='2024-01-21'
    url = 'https://api.codelife.cc/api/weather/city?lang=cn&location='+local
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
        'Authorization': 'Token eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2MjExZWExOThmODk3ZDNhZGZiMWM3NTMiLCJpYXQiOjE3MDU5MDI3OTQsImV4cCI6MTczNzAwNjc5NH0.CjKNQfnjHQ3pofI94wkKuLHiyB_EeVFpQ6BhpC8QKY4',
        'Signaturekey': 'U2FsdGVkX19fsjh/WEtSmaTFRMkg3D94ZyAS4wwFazI='
    }
    response = requests.get(url, headers=headers).json()['data'][0]['id']
    url1='https://api.codelife.cc/api/getWeather?lang=cn&location='+response
    response = requests.get(url1, headers=headers)
    if response.status_code == 200:
        data = response.json()['data']
        tmp=data['now']['tmp']
        pres=data['now']['pres']
        cond_txt=data['now']['cond_txt']
        wind_dir=data['now']['wind_dir']
        wind_sc=data['now']['wind_sc']
        hum=data['now']['hum']
        pcpn=data['now']['pcpn']
        lifestyle=data['lifestyle']
        qlty=data['air_now_city']['qlty']
        aqi=data['air_now_city']['aqi']
        comf=lifestyle[0]['brf']
        drsg=lifestyle[1]['brf']
        flu=lifestyle[2]['brf']
        trav=lifestyle[3]['brf']
        uv=lifestyle[4]['brf']
        cw=lifestyle[5]['brf']
        fsh=lifestyle[6]['brf']
        txt=data['rain']['txt']
        daily_forecast=data['daily_forecast'][0]
        tmp_min=daily_forecast['tmp_min']
        tmp_max=daily_forecast['tmp_max']
        ss=daily_forecast['ss']
        sr=daily_forecast['sr']
        fileurl=folder+'/img_name.json'
        with open(fileurl, 'r') as f:
            fileurls = json.load(f)
        imgurl = list(set(fileurls))
        txt='<!DOCTYPE html><html lang="en"><head>    <meta charset="UTF-8" />   <style> .fristimg {width: 18px;height: 18px;vertical-align: -4px;}.f12 {font-size: 12px}.ma20 {margin: 20px;}img{display: list-item;text-align: -webkit-match-parent;}li {display: list-item;text-align: -webkit-match-parent;}.bgcode{width: 650px;}.life {padding: 12px;border-radius: 6px;background-color: #ffffff08;display: grid;grid-template-columns: repeat(4, 1fr);line-height: 16px;}.timg {width: 300px;/* height: 100px; */border-radius: 6px;}.simg {width: 24px;height: 24px;vertical-align: -4px;margin-left: 20px;}.s1img {width: 18px;height: 18px;vertical-align: -4px;}.text {font-size: 80px;line-height: 80px;height: 80px}.ml20 {margin-left: 20px;}.br1 {background-color: antiquewhite;border-radius: 6px;}.mr20 {margin-right: 20px;}.mt20 {margin-top: 20px;}.p9 {padding: 9px;}.mb20 {margin-bottom: 20px;}.sflex {display: flex;align-items: center;}.br5 {border-radius: 5px;background-color: aliceblue;}ol,ul {list-style: none}.sa {display: flex;align-items: center;}.kkk {width: 600px;}.c1 {color: #5fc7fb;padding: 8px;}.con{width: 650px;}.sssa {font-size: 12px;margin-bottom: -10px;box-sizing: border-box;padding-top: 20px;padding-left: 10px;border: 0;font: inherit;display: flex;align-items: center;}.tpimg {display: grid;grid-template-columns:repeat(2,300px);margin: 20px;align-items: center;grid-gap: 10px;}</style></head><body>    <div class="ma20 bgcode br5">        <div>            <div class="br5 p9">                <div class="ma20">                    <span>四川省&nbsp;·&nbsp;</span><span>渠县</span>&nbsp;&nbsp;<span>'+cond_txt+'</span><span>&nbsp;&nbsp;&nbsp;发布于&nbsp;:&nbsp;'+formatted_date+'&nbsp;                        '+time+'</span> </div>            </div>            <div class="sflex ml20"> <span class="text ml20">'+tmp+'°</span>                <div class="ml20">                    <p> <i> <img class="fristimg" src="https://cdn.jsdelivr.net/gh/Codebglh/img/test/yezi.svg" /> </i>                        '+qlty+'/'+aqi+' </p>                    <p> <img class="fristimg" src="https://cdn.jsdelivr.net/gh/Codebglh/img/test/sun.svg" />                        <span>'+cond_txt+'</span> <span>'+wind_dir+'</span> <span>'+wind_sc+'级</span> </p>                </div>            </div>            <div class="br5 ml20 mt20 c1">'+txt+'</div>            <div class="br5 ml20 c1"> <span>温度 '+tmp_min+'°~'+tmp_max+'°</span> <span>湿度 '+hum+'%</span> <span>气压 '+pres+'hPa</span> <span>降水                    '+pcpn+'mm</span> <span>日出&nbsp;'+sr+'</span> <span>日落&nbsp;'+ss+'</span> </div>            <div class="f12 ma20 br1 kkk">                <h4 class="sssa"> <i> <img class="s1img" src="https://cdn.jsdelivr.net/gh/Codebglh/img/test/life.svg" />                    </i>生活指数 </h4>                <ul class="life">                    <li>                        <div class="sa"> <span> <i> <img class="simg"                                        src="https://cdn.jsdelivr.net/gh/Codebglh/img/test/susi.svg" /> </i></span>                            <dl class="ml20">                                <dt>'+comf+'</dt>                                <dt>舒适度指数</dt>                            </dl>                        </div>                    </li>                    <li>                        <div class="sa"> <span><i><img class="simg"                                        src="https://cdn.jsdelivr.net/gh/Codebglh/img/test/cy.svg" /> </i></span>                            <dl class="ml20">                                <dt>'+drsg+'</dt>                                <dt>穿衣指数</dt>                            </dl>                        </div>                    </li>                    <li>                        <div class="sa"> <span><i><img class="simg"                                        src="https://cdn.jsdelivr.net/gh/Codebglh/img/test/gm.svg" /> </i></span>                            <dl class="ml20">                                <dt>'+flu+'</dt>                                <dt>感冒指数</dt>                            </dl>                        </div>                    </li>                    <li>                        <div class="sa"> <span><i><img class="simg"                                        src="https://cdn.jsdelivr.net/gh/Codebglh/img/test/ly.svg" /> </i></span>                            <dl class="ml20">                                <dt>'+trav+'</dt>                                <dt>旅游指数</dt>                            </dl>                        </div>                    </li>                    <li>                        <div class="sa"> <span><i><img class="simg"                                        src="https://cdn.jsdelivr.net/gh/Codebglh/img/test/zwx.svg" /> </i></span>                            <dl class="ml20">                                <dt>'+uv+'</dt>                                <dt>紫外线指数</dt>                            </dl>                        </div>                    </li>                    <li>                        <div class="sa"> <span><i><img class="simg"                                        src="https://cdn.jsdelivr.net/gh/Codebglh/img/test/xc.svg" /> </i></span>                            <dl class="ml20">                                <dt>'+cw+'</dt>                                <dt>洗车指数</dt>                            </dl>                        </div>                    </li>                    <li>                        <div class="sa"> <span><i><img class="simg"                                        src="https://cdn.jsdelivr.net/gh/Codebglh/img/test/dy.svg" /> </i></span>                            <dl class="ml20">                                <dt>'+fsh+'</dt>                                <dt>钓鱼指数</dt>                            </dl>                        </div>                    </li>                </ul>            </div>        </div>        <div class="con">            <div class="tpimg">  <img class="timg"            src="'+imgurl[0]+'" />        <img class="timg"            src="'+imgurl[1]+'" />        <img class="timg"            src="'+imgurl[2]+'" />        <img class="timg"            src="'+imgurl[3]+'" />            <img class="timg"            src="'+imgurl[4]+'" />        <img class="timg"            src="'+imgurl[5]+'" />        <img class="timg"            src="'+imgurl[6]+'" />        <img class="timg"            src="'+imgurl[7]+'" />        <img class="timg"            src="'+imgurl[8]+'" />        <img class="timg"            src="'+imgurl[9]+'" />        <img class="timg"            src="'+imgurl[10]+'" />        <img class="timg"            src="'+imgurl[11]+'" />            <img class="timg"            src="'+imgurl[12]+'" />        <img class="timg"            src="'+imgurl[13]+'" />        <img class="timg"            src="'+imgurl[14]+'" />        <img class="timg"            src="'+imgurl[15]+'" />        <img class="timg"            src="'+imgurl[16]+'" />        <img class="timg"            src="'+imgurl[17]+'" />        <img class="timg"            src="'+imgurl[18]+'" />        <img class="timg"            src="'+imgurl[19]+'" />  </div>        </div>    </div></body></html>'
    else:
        print('Failed to fetch data.')
  
    return txt


def write_text_to_file(text):
    with open('text.html', 'w') as f:
        f.write(text)
write_text_to_file(getWeather('渠县'))
# getWeather('渠县')