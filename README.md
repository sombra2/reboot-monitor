# Reboot monitor

A simple python script that will alert you on telegram when the computer you host it on reboots. Very useful for home servers, raspberry pi, etc. I have been using it for some time now in a home raspberry kit to detect when the power has gone. It helps me recognize if I have to restart any services.

## Creation of a credentials.py file

You will have to create a separate `credentials.py` file once you clone the repository. In this file you must include the following variables:

  `bot_token` - this is the ID of the bot you plan on using as alert, full information on Telegram Bots and API can be found [here](https://core.telegram.org/bots)
  
  `bot_chatID` - this is the ID of the group chat you plan the bot to alert you on, full information on Telegram Bots and API can be found [here](https://core.telegram.org/bots)
  
  `ip_api` - this is the token given to you to access all the geodata associated to the IP of your machine. I have chosen [Abstract IP Geolocation API](https://www.abstractapi.com/ip-geolocation-api) for this project. You can create a free account and obtain your token as long as you don't do more than one request per second (as of September 2021)

The script will call these 3 variables

## Deployment

I would advise deploying the file `reboot.py` somewhere in your machine, then run it through a cron task such as `@reboot sleep 60 && reboot.py`, that way the script will initialize when your machine restarts, it will wait 60 seconds (to gain internet access) and then will send the request to the Telegram API to send you the message.

## Acknowledgements

Please bear in mind that this is a very tiny learning project I have done for myself, there might be flaws and defects but I am still learning. 

Special thanks to the [Public APIs repository](https://github.com/public-apis/public-apis)
