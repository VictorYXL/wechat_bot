from WXBot import *
from apscheduler.schedulers.blocking import BlockingScheduler 

class Scheduler:
    wxbot = None
    sched = BlockingScheduler()
    def __init__(self, wxbot: WXBot):
        self.wxbot = wxbot
    
    def regular_job_per_hour(self, message: str, hour_str: str = '9-17') -> None:
        self.sched.add_job(wxbot.send_message, args = [message], trigger = 'cron', hour=hour_str)
    
    def start(self) -> None:
        self.sched.start()

if __name__ == '__main__':
    wxbot = WXBot('yxl')
    sche = Scheduler(wxbot)
    sche.regular_job_per_hour('别坐太久')
    sche.start()