from wxpy import *
from apscheduler.schedulers.blocking import BlockingScheduler 
class WXBot:
    # wechat bot
    bot = None
    # friend or group
    chat_object = None

    def __init__(self):
        # Login with cache
        self.bot = Bot(cache_path=True)
        return None
    
    def search_friend(self, friend_name: str) -> str:
        # Search friend first
        friend_list = self.bot.friends().search(friend_name)
        if len(friend_list) > 0:
            self.chat_object = friend_list[0]
            return self.chat_object.name
        
        #Search group when no friend found
        group_list = self.bot.groups().search(friend_name)
        if len(group_list) > 0:
            self.chat_object = group_list[0]
            return self.chat_object.name
        
        # No friend or group found
        raise 'No group ' + friend_name + ' found.'
    
    def send_message(self, message: str) -> None:
        if self.chat_object == None:
            raise 'No send object'
        self.chat_object.send('聊天机器人小杨: ' + message)

if __name__ == '__main__':
    wxbot = WXBot()
    wxbot.search_friend('家人')
    wxbot.send_message('你好')