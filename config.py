#API Key from trafiklab.se
DEVIATION_API_KEY = "6834613731213fe72d269d4a34d1bb55"

#Different kinds of transport modes, can not be None.
#Available params: metro, tram, bus, train
TRANSPORT_MODE = 'metro'

#Comma seperated lists of lines you want to track.
#Possible to be None
TRANSPORT_LINES = None

#Don't check deviation after this hour
#Expected format: HH:MM:SS
LAST_TIME_TO_CHECK = '22:00:00'

#Time to start again if you have stopped watching after a certain hour
#Expected format: HH:MM:SS
FIRST_TIME_TO_CHECK = '06:00:00'

#Send email alerts
SEND_ALERT = False

#Receiver of the email alerts
ALERT_RECEIVER = ''

#Who should the alert be from
ALERT_SENDER = ''

SAVE_DEVIATION = True

MYSQL_HOST = ''

MYSQL_USER = ''

MYSQL_PASSWORD = ''

MYSQL_DATABASE = ''
