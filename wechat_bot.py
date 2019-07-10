from wxpy import *
from log import *
class Wechat_Bot:
    # wechat bot
    bot = None
    # friend or group
    friend = None
    friend_name = None

    def __init__(self, friend_name):
        # Login with cache
        self.bot = Bot(cache_path=True)
        self.friend_name = friend_name

        # Search friend first
        friend_list = self.bot.friends().search(friend_name)
        if len(friend_list) > 0:
            self.friend = friend_list[0]
            return None
        # Search group when no friend found
        group_list = self.bot.groups().search(friend_name)
        if len(group_list) > 0:
            self.friend = group_list[0]
            return None
        # File helper
        if friend_name == 'file_helper':
            self.friend = self.bot.file_helper
            return None
            
        # No friend or group found
        raise 'No group ' + friend_name + ' found.'
    
    def send_message(self, message: str) -> None:
        self.friend.send('[机器人小亮] ' + message)
        send_message_log(self.friend_name, message)

    def send_image(self, image_path: str) -> None:
        self.friend.send_image(image_path)
        send_image_log(self.friend_name, image_path)
    
    def send_voice(self, voice_path: str) -> None:
        self.friend.send_file(voice_path)
        send_voice_log(self.friend_name, voice_path)

if __name__ == '__main__':
    wxbot = Wechat_Bot('file_helper')
    wxbot.send_voice('src\\easy_english\\1\\1\\voice.mp3')