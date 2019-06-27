import requests
import json
import random
from bs4 import BeautifulSoup

# Get weather from http://wthrcdn.etouch.cn/weather_mini
# date: today or tomorrow
def grab_weather(date: str, city: str) -> dict:
    weather_site = 'http://wthrcdn.etouch.cn/weather_mini'
    request_url = weather_site + '?city=' + city
    response = requests.get(request_url)
    response_dict = json.loads(response.text)
    if date == 'today':
        weather_dict = response_dict['data']['forecast'][0]
        date_str = city + '今天'
    elif date == 'tomorrow':
        weather_dict = response_dict['data']['forecast'][1]
        date_str = city + '明天'
    weather_type = weather_dict['type']
    high_tem = weather_dict['high'][3:5]
    low_tem = weather_dict['low'][3:5]
    if weather_dict['fengli'][9]  in ['<', '>']:
        wind_power = weather_dict['fengli'][9:12]
    else:
        wind_power = weather_dict['fengli'][9:13]
    weather_str = date_str + '天气' +  weather_type + ', 最高温' + high_tem + '℃ ， 最低温'  + low_tem + '℃ ， 风力' + wind_power
    return weather_str

# Get joke from http://duanziwang.com
def grab_joke():
    joke_site = 'http://duanziwang.com'
    joke_index = random.randint(0, 1000)
    request_url = joke_site + '/' + str(joke_index) + '.html'
    response = requests.get(request_url)
    soup = BeautifulSoup(response.text,  'html.parser')
    joke_str = soup.find_all('section', class_ = 'post-content')[0].get_text().replace('\n', '')
    return joke_str


if __name__ == "__main__":
    #print(get_weather('北京', 'today'))
    print(grab_joke())