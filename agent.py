from wechat_bot import Wechat_Bot
from infomation_getter import Information_Getter

# Store 1 wechat_bot and share info_getter with other agents
class Agent:
    info_getter = None
    friend_bot = None
    friend_city = None
    easy_word_index = 0
    def __init__(self, friend_name: str, friend_city: str, info_getter: Information_Getter):
        self.friend_bot = Wechat_Bot(friend_name)
        self.info_getter = info_getter
        self.friend_city = friend_city
    
    def send_weather(self, date: str) -> None:
        weather_dict = self.info_getter.get_weather(city = self.friend_city)
        if date == 'today':
            '早安, ' + self.friend_bot.friend_name + '。 '
        else:
            '晚安, ' + self.friend_bot.friend_name + '。 '
        self.friend_bot.send_message('为您播报天气预报')
        self.friend_bot.send_message(weather_dict[date])
        self.friend_bot.send_message(weather_dict['tip'])
        
        return None
    
    def send_joke(self) -> None:
        joke_str = self.info_getter.get_joke()
        self.friend_bot.send_message('给您说个笑话吧')
        self.friend_bot.send_message(joke_str)
        return None
    
    def send_image(self) -> None:
        image_path = self.info_getter.get_image()
        self.friend_bot.send_message('工作之余，看个风景吧')
        self.friend_bot.send_image(image_path)
    
    def send_easy_word_subject(self) -> None:
        self.friend_bot.send_message('今天要学英语哦')
        self.friend_bot.send_message('今天学习的主题是' + self.info_getter.get_easy_word_subject())
        self.easy_word_index = 0

    def send_easy_word(self) -> None:
        word_dict = self.info_getter.get_easy_word(self.easy_word_index)
        self.friend_bot.send_message('请跟我学: ' + word_dict['chi'] + ', ' + word_dict['eng'])
        self.friend_bot.send_image(word_dict['image'])
        self.friend_bot.send_voice(word_dict['voice'])
        self.easy_word_index += 1



if __name__ == "__main__":
    info_getter = Information_Getter()
    agent = Agent(friend_name = 'file_helper', friend_city = '北京', info_getter = info_getter)
    agent.send_easy_word()
    
    