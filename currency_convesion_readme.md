# ConversionRate Fetcher

* This module is to fetch conversion rates between two sites and send the alert to user via telegram.

## Prerequistes:

1. Environment OS , mac linux or windows
2. Python 3.6 or above
3. Chrome 98.0X 


## Installation : 

1. Install requirements from requirements.txt (Pip install -r requirements.txt)
2. Change os value to appropriate os for picking chromedriver (linux,mac or windows)
3. Install telegram and signup on your smart phone
4. Add the bot @conversion_notifier_bot and press start on your mobile.
5. Pin the bot on top to get immediate notifications and change settings to always notify for alerts if required.
6. Run show_hashkey.py to get the hash key value which gives complete control on the bot (python show_hashkey.py)
7. In the terminal type telegram-send --configure to input hash key to start controlling the bot.
8. You can start running the application to get alerts with following command (python fetchrate.py)
9. Schedule the above command in corresponding box in cloud to start getting daily alerts on your smartphone


## BotFather

1. Open botfather in telegram
2. press start
3. create bot using /newbot
4. choose name for bot
5. choose userid for bot
6. press help for more options
7. set display pic,description and name accordingly. (\setuserpic,\setname,\setdescription).
8. generate token with help of \token
9. once token generated, key in the token using telegram-send --config comand to get passcode.
10. Go to corresponding bot in telegram press /start and give passcode. Voila.. The bot is now your to control through scripts. 