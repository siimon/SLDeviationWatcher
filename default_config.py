#API Key from trafiklab.se
DEVIATION_API_KEY = "6834613731213fe72d269d4a34d1bb55"

#Different kinds of transport modes, can not be None.
#Available params: metro, tram, bus, train
TRANSPORT_MODE = 'metro'

#Comma seperated lists of lines you want to track.
#Possible to be None
TRANSPORT_LINES = None

#Array of start and stop times, only check for deviations between these intervals
INTERVAL_TIMES = [ { 'start':'07:00:00', 'stop': '09:00:00' }, { 'start': '15:00:00', 'stop':'18:00:00' } ]

#Send email alerts
SEND_ALERT = True 

#Receiver of the email alerts
ALERT_RECEIVER = ''

#Who should the alert be from
ALERT_SENDER = ''

#Save deviation to DB. See DB script to create DB.
SAVE_DEVIATION = True

#MySQL host
MYSQL_HOST = ''

#MySQL user
MYSQL_USER = ''

#MySQL pass
MYSQL_PASSWORD = ''

#MySQL Database
MYSQL_DATABASE = 'SLDeviation'

#PushOver integration, create a free account on pushover.net
#Enable notifications, send on major disruptions only
PUSHOVER_SEND_PUSH_NOTIFICATIONS = True

#PushOver user key 
PUSHOVER_USER_KEY = ''

#PushOver app key for this application
PUSHOVER_APP_KEY = ''

