import time

def get_date() -> str:
    return time.strftime("%Y-%m-%d", time.localtime())

def get_time() -> str:
    return time.strftime("%H:%M:%S", time.localtime())

def send_message_log(friend_name: str, message: str) -> None:
    log_file = open('log/' + get_date() + '.txt', 'a+')
    log_file.write(get_time() + ' send message to ' + friend_name + ':\n    ')
    log_file.write(message + '\n')
    log_file.close()
    return None

def grab_weather_log(city: str, website: str, weather_tip_dict: dict) -> None:
    log_file = open('log/' + get_date() + '.txt', 'a+')
    log_file.write(get_time() + 'grab ' + city + ' weather from ' + website + ':\n    ')
    log_file.write(weather_tip_dict['today'] + '\n    ')
    log_file.write(weather_tip_dict['tomorrow'] + '\n    ')
    log_file.write(weather_tip_dict['tip'] + '\n')
    log_file.close()

def grab_joke_log(website: str, joke_str: str) -> None:
    log_file = open('log/' + get_date() + '.txt', 'a+')
    log_file.write(get_time() + 'grab joke from ' + website + ':\n    ')
    log_file.write(joke_str + '\n')
    log_file.close()

