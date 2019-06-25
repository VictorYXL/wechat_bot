from agent import Agent

def agent_wife():
    agent = Agent('女神', '北京')
    agent.add_send_weather_job()
    agent.add_send_joke_job()
    agent.start()    

def agent_family():
    agent = Agent('家人', '芜湖')
    agent.add_send_weather_job()
    agent.add_send_joke_job()
    agent.start()

def agent_test():
    agent = Agent('file_helper', '北京')
    agent.add_send_weather_job()
    agent.add_send_joke_job()
    agent.start()

if __name__ == '__main__':
    agent_wife()
    #agent_family()
    