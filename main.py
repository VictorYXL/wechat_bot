from agent import Agent_Base

if __name__ == '__main__':
    agent = Agent_Base('女神', '北京')
    #agent = Agent_Base('家人', '芜湖')
    #agent = Agent_Base('yxl', '家人')
    #agent = Agent_Base('file_helper', '北京')
    agent.add_send_weather_job()
    agent.add_send_joke_job()
    agent.start()