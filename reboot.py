# This script is completely functiontal as it is. It just sends a ping message to your telegram to tell
# you that the machine has rebooted

import requests
import datetime
# the credentials.py file is not here, you will have to create your own with the variables related to bot_token,
# bot_chatID and ip_token for the geo ip api service
import credentials

now = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
device = 'MacBook Pro' # name here the device the way you want it to show up in your telegram message todo retrieve hostname

def retrieve_geoipdata():
  response = requests.get("https://ipgeolocation.abstractapi.com/v1/?api_key=" + credentials.ip_api)
  print(response.content)


def telegram_bot_sendtext(bot_message):
  send_text = 'https://api.telegram.org/bot' + credentials.bot_token + '/sendMessage?chat_id=' + credentials.bot_chatID + '&parse_mode=markdown&text=' + bot_message
  response = requests.get(send_text)
  return response.json()

#telegram_bot_sendtext('{} at [{}] -=REBOOT=- on {}'.format(device,ip,now))
retrieve_geoipdata()