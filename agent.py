from apscheduler.schedulers.blocking import BlockingScheduler 
from component import Component

class Agent_Base:
    component = None
    sched = None

    def __init__(self, friend_name: str, friend_city: str) -> None:
        self.component = Component(friend_name, friend_city)
        self.sched = BlockingScheduler()
    
    def add_send_weather_job(self) -> None:
        self.sched.add_job(self.component.send_weather, args = ['today'], trigger = 'cron', hour = '7')
        self.sched.add_job(self.component.send_weather, args = ['tomorrow'], trigger = 'cron', hour = '22')
    
    def add_send_joke_job(self) -> None:
        self.sched.add_job(self.component.send_joke, args = [''], trigger = 'cron', hour = '10, 12, 14, 16, 18')
    
    def start(self) -> None:
        # TODO: use multi-thread
        self.sched.start()