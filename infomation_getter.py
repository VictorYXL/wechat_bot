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
    landscape_index = 0
    easy_word_subject_index = 0
    def get_weather(self, city = '北京') -> list:
        if self.weather.get(city) == None:
            self.weather[city] = {}
            self.update_weather(city = city)
        return self.weather[city]

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
    
    def get_image(self) -> str:
        return 'src\\landscape\\' + str(self.landscape_index) + '.jpg'

    def update_image(self) -> None:
        self.landscape_index += 1

    def get_easy_word_subject(self) -> str:
        subject_file = 'src\\easy_word\\' + str(self.easy_word_subject_index) + '\\subject.txt'
        file = open(subject_file, 'r', encoding = 'utf8')
        subject_name = file.read()
        file.close()
        return subject_name

    def get_easy_word(self, word_index) -> dict:
        word_dir = 'src\\easy_word\\' + str(self.easy_word_subject_index) + '\\' + str(word_index) + '\\'
        word_file = word_dir + 'word.txt'
        file = open(word_file, 'r', encoding = 'utf8')
        eng_word = file.readline()
        chi_word = file.readline()
        image_path = word_dir + 'image.jpg'
        voice_path = word_dir + 'voice.mp3'
        file.close()
        word_dict = {'eng': eng_word, 'chi': chi_word, 'image': image_path, 'voice': voice_path}
        return word_dict
    
    def update_easy_word_index(self) -> None:
        self.easy_word_subject_index += 1


        
        #self.easy_word_subject_index

    

        
if __name__ == "__main__":
    info_getter = Information_Getter()
    info_getter.get_easy_word(1)

