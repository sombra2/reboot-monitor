# This script is completely functiontal as it is. It just sends a ping message to your telegram to tell
# you that the machine has rebooted

import os
import requests
import datetime
import json
# the credentials.py file is not here, you will have to create your own with the variables related to bot_token,
# bot_chatID and ip_token for the geo ip api service
import credentials

now = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
device = os.uname()[1].split('.')[0] # we get the hostname without extension here

response = requests.get('https://ipgeolocation.abstractapi.com/v1/?api_key=' + credentials.ip_api)
response = json.loads(response.content) # parses the json object into a python dictionary
ip_address = response['ip_address']
city = response['city']
emoji = response['flag']['emoji']

def telegram_bot_sendtext(bot_message):
  send_text = 'https://api.telegram.org/bot' + credentials.bot_token + '/sendMessage?chat_id=' + credentials.bot_chatID + '&parse_mode=markdown&text=' + bot_message
  response = requests.get(send_text)
  return response.json()

telegram_bot_sendtext('<b>{}</b> at {} ({} {}) -=REBOOT=- on {}'.format(
  device,
  ip_address,
  city,
  emoji,
  now))
