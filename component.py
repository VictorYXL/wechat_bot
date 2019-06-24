
from wechat_bot import Wechat_Bot
from infomation_getter import Infomation_Getter
class Component:
    wechat_bot = None
    infomation_getter = None
    friend_city = ''
    
    def __init__(self, friend_name: str, friend_city: str = ''):
        self.wechat_bot = Wechat_Bot(friend_name)
        self.infomation_getter = Infomation_Getter()
        self.friend_city = friend_city
        return None
    
    def send_weather(self, date: str) -> None:
        if self.friend_city != '':
            weather_str = self.infomation_getter.get_weather(self.friend_city, date)
            if date == 'today':
                self.wechat_bot.send_message('为您播报今天天气')
            elif date == 'tomorrow':
                self.wechat_bot.send_message('为您播报明天天气')
            self.wechat_bot.send_message(weather_str)
        return None

    