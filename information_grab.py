import requests
import json
import random
from bs4 import BeautifulSoup
from log import *

# Get weather from http://wthrcdn.etouch.cn/weather_mini
# date: today or tomorrow
def analyze_weather(weather_dict) -> str:
    weather_type = weather_dict['type']
    high_tem = weather_dict['high'][3:5]
    low_tem = weather_dict['low'][3:5]
    if weather_dict['fengli'][9]  in ['<', '>']:
        wind_power = weather_dict['fengli'][9:12]
    else:
        wind_power = weather_dict['fengli'][9:13]
    weather_str = '天气' +  weather_type + '， 最高温' + high_tem + '℃ ， 最低温'  + low_tem + '℃ ， 风力' + wind_power
    return weather_str

def grab_weather(city: str) -> dict:
    # { 'today': xxx, 'tomorrow': xxx, 'tip': xxx}
    weather_site = 'http://wthrcdn.etouch.cn/weather_mini'
    request_url = weather_site + '?city=' + city
    response = requests.get(request_url)

    response_dict = json.loads(response.text)
    weather_dict_today = response_dict['data']['forecast'][0]
    weather_dict_tomorrow = response_dict['data']['forecast'][1]

    today_str = city + '今天' + analyze_weather(weather_dict_today)
    tomorrow_str = city + '明天' + analyze_weather(weather_dict_tomorrow)
    weather_tip = response_dict['data']['ganmao']

    weather_tip_dict = {'today': today_str, 'tomorrow': tomorrow_str, 'tip': weather_tip}    
    grab_weather_log(city = city, website = request_url, weather_tip_dict = weather_tip_dict)
    return weather_tip_dict

# Get joke from http://duanziwang.com
def grab_joke():
    joke_site = 'http://duanziwang.com'
    joke_index = random.randint(0, 1000)
    request_url = joke_site + '/' + str(joke_index) + '.html'
    response = requests.get(request_url)
    soup = BeautifulSoup(response.text,  'html.parser')
    joke_str = soup.find_all('section', class_ = 'post-content')[0].get_text().replace('\n', '')
    grab_joke_log(request_url, joke_str)
    return joke_str


if __name__ == "__main__":
    print(grab_weather(city = '芜湖'))
    #print(grab_joke())