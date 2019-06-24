from wxpy import *
class WXBot:
    # wechat bot
    bot = None
    # friend or group
    chat_object = None

    def __init__(self, friend_name):
        # Login with cache
        self.bot = Bot(cache_path=True)

        # Search friend first
        friend_list = self.bot.friends().search(friend_name)
        if len(friend_list) > 0:
            self.chat_object = friend_list[0]
        else:
            #Search group when no friend found
            group_list = self.bot.groups().search(friend_name)
            if len(group_list) > 0:
                self.chat_object = group_list[0]
            else:        
                # No friend or group found
                raise 'No group ' + friend_name + ' found.'
    
    def send_message(self, message: str) -> None:
        if self.chat_object == None:
            raise 'No send object'
        self.chat_object.send('聊天机器人小杨: ' + message)
    
    def log(self, log_message: str) -> None:
        file = open(self.chat_object.name + ".txt", "w+")
        file.write(log_message + '\n')
        file.close()


if __name__ == '__main__':
    wxbot = WXBot('女神')
    wxbot.send_message('你好')