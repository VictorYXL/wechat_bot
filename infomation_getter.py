from information_grab import *
class Information_Getter:
        #self.waether = 
        # {
        #   'city_1': 
        #   {
        #       'today': weather_str_today, 
        #       'tomorrow': weather_str_tomorrow,
        #       'tip': weather_tip
        #    },
        #   'city_2': 
        #   {
        #       'today': weather_str_today, 
        #       'tomorrow': weather_str_tomorrow,
        #       'tip': weather_tip
        #    },
        # }
    weather = {}
    joke = ''
    def get_weather(self, city = '北京', date = 'today') -> list:
        if self.weather.get(city) == None:
            self.weather[city] = {}
            self.update_weather(city = city)
        return self.weather[city][date]

    def update_weather(self, city = '北京') -> None:
        self.weather[city] = {}
        while self.weather[city] == {}:
            self.weather[city] = grab_weather(city = city)

    def get_joke(self) -> str:
        return self.joke

    def update_joke(self) -> str:
        self.joke = ''
        while self.joke == '':
            self.joke = grab_joke()
        
if __name__ == "__main__":
    info_getter = Information_Getter()
    info_getter.update_weather(city = '芜湖')
    print(info_getter.get_weather(city = '芜湖', date = 'today'))

