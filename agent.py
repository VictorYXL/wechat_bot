from apscheduler.schedulers.blocking import BlockingScheduler 
from WXBot import WXBot
from component import Component

def agent_common(object: str) -> None:
    wxbot = WXBot('yxl')
    sched = BlockingScheduler()
    component = Component(wxbot)

    sched.add_job(component.send_weather, args = ['北京', 'today'], trigger = 'cron', hour='7')
    sched.add_job(component.send_weather, args = ['北京', 'tomorrow'], trigger = 'cron', hour='22')
    sched.start()
    return None

def agent_my_wife():
    return None

def agent_family():
    return None

def agent_myself():
    return None

if __name__ == '__main__':
     agent_common('女神')
    # agent_common('家人')
    # agent_common('yxl')