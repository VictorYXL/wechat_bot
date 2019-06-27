from information_grab import *
class Information_Getter:
    weather = None
    joke = ''
    def __init__(self):
        self.weather = {'today': {}, 'tomorrow': {}}
        self.update_joke()

    def get_weather(self, date = 'today', city = '北京') -> str:
        if self.weather[date].get(city) == None:
            self.weather[date][city] = ''
            self.update_weather(date, city)
        return self.weather[date][city]

    def update_weather(self, date = 'today', city = '北京') -> None:
        self.weather[date][city] = ''
        while self.weather[date][city] == '':
            self.weather[date][city] = grab_weather(date, city)

    def get_joke(self) -> str:
        return self.joke

    def update_joke(self) -> str:
        self.joke = ''
        while self.joke == '':
            self.joke = grab_joke()
        
if __name__ == "__main__":
    info_getter = Information_Getter()
    print(info_getter.get_weather(date = 'tomorrow', city = '芜湖'))

