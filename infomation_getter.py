import requests
import json

class Infomation_Getter:
    # date: today or tomorrow
    def get_weather(self, city: str, date: str) -> dict:
        weather_site = 'http://wthrcdn.etouch.cn/weather_mini'
        request_url = weather_site + '?city=' + city
        response = requests.get(request_url)
        response_dict = json.loads(response.text)
        if date == 'today':
            weather_dict = response_dict['data']['forecast'][0]
            date_str = '今天'
        elif date == 'tomorrow':
            weather_dict = response_dict['data']['forecast'][1]
            date_str = '明天'
        weather_type = weather_dict['type']
        high_tem = weather_dict['high'][3:5]
        low_tem = weather_dict['low'][3:5]
        wind_power = weather_dict['fengli'][9:12]
        weather_str = date_str + '天气' +  weather_type + ', 最高温' + high_tem + '℃ ， 最低温'  + low_tem + '℃ ， 风力' + wind_power + '级。'
        return weather_str

if __name__ == "__main__":
    print(Infomation_Getter().get_weather('北京', 'today'))