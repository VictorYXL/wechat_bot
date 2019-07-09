from apscheduler.schedulers.blocking import BlockingScheduler 
from infomation_getter import Information_Getter
from agent import Agent
class Scheduler:
    sched = None
    info_getter = None

    def __init__(self, info_getter: Information_Getter) -> None:
        self.sched = BlockingScheduler()
        self.info_getter = info_getter
    
    def add_send_weather_job(self, agent: Agent) -> None:
        self.sched.add_job(func = agent.send_weather, args = ['today'], trigger = 'cron', hour = '7')
        self.sched.add_job(func = agent.send_weather, args = ['tomorrow'], trigger = 'cron', hour = '22')
    
    def add_send_joke_job(self, agent: Agent) -> None:
        self.sched.add_job(func = agent.send_joke, trigger = 'cron', hour = '10, 12, 14, 16, 18')
    
    def add_update_joke_job(self) -> None:
        self.sched.add_job(func = self.info_getter.update_joke, trigger = 'cron', hour = '10, 12, 14, 16, 18', minute = '5')
    
    def add_send_image_job(self, agent: Agent) -> None:
        self.sched.add_job(func = agent.send_image, trigger = 'cron', hour = '9, 11, 13, 15, 17')

    def add_update_image_job(self) -> None:
        self.sched.add_job(func = self.info_getter.update_image, trigger = 'cron', hour = '9, 11, 13, 15, 17', minute = '5')
    
    def start(self) -> None:
        self.sched.start()

if __name__ == "__main__":
    info_getter = Information_Getter()
    agent_1 = Agent(friend_name = 'file_helper', friend_city = '北京', info_getter = info_getter)
    agent_2 = Agent(friend_name = '女神', friend_city = '北京', info_getter = info_getter)
    scheduler = Scheduler(info_getter = info_getter)
    scheduler.add_send_joke_job(agent = agent_1)
    scheduler.add_send_joke_job(agent = agent_2)
    scheduler.add_update_joke_job()
    scheduler.start()