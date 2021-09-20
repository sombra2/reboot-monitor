# This script is completely funciontal as it is. It just sends a ping message to your telegram to tell you that the machine has rebooted

import requests
import datetime
import credentials

now = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
location = 'unknown' # todo for the next edit
ip = requests.get('https://api.ipify.org').text # todo change api
device = 'MacBook Pro' # name here the device the way you want it to show up in your telegram message # todo retrieve hostname

def telegram_bot_sendtext(bot_message):
  send_text = 'https://api.telegram.org/bot' + credentials.bot_token + '/sendMessage?chat_id=' + credentials.bot_chatID + '&parse_mode=markdown&text=' + bot_message
  response = requests.get(send_text)
  return response.json()

telegram_bot_sendtext('{} at [{}] -=REBOOT=- on {}'.format(device,ip,now))