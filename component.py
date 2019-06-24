
from WXBot import WXBot
from get_infomation import get_weather
class Component:
    wxbot = None
    def __init__(self, wxbot: WXBot):
        self.wxbot = wxbot
        return None
    
    def send_weather(self, city: str, date: str) -> None:
        weather_str = get_weather(city, date)
        if date == 'today':
            self.wxbot.send_message('为您播报今天天气')
        elif date == 'tomorrow':
            self.wxbot.send_message('为您播报明天天气')
        self.wxbot.send_message(weather_str)
        return None

    