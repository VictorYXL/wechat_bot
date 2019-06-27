from agent import Agent
from infomation_getter import Information_Getter
from scheduler import Scheduler

def main():
    # Init 
    info_getter = Information_Getter()
    agent_wife = Agent(friend_name = '女神', friend_city = '北京', info_getter = info_getter)
    agent_family = Agent(friend_name = '家人', friend_city = '芜湖', info_getter = info_getter)
    scheduler = Scheduler(info_getter)

    # Add task
    scheduler.add_send_weather_job(agent_wife)
    scheduler.add_send_weather_job(agent_family)
    scheduler.add_send_joke_job(agent_wife)
    scheduler.add_update_joke_job()

    # Run
    scheduler.start()

def test():
    info_getter = Information_Getter()
    agent_test = Agent(friend_name = 'file_helper', friend_city = '北京', info_getter = info_getter)
    scheduler = Scheduler(info_getter)
    scheduler.add_send_joke_job(agent_test)
    scheduler.add_send_weather_job(agent_test)
    scheduler.start()


if __name__ == '__main__':
    main()

