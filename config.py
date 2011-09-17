#API Key from trafiklab.se
DEVIATION_API_KEY = ""

#Different kinds of transport modes, can not be None.
#Available params: metro, ?? , ?? , ??
TRANSPORT_MODE = 'metro'

#Comma seperated lists of lines you want to track.
#Possible to be None
TRANSPORT_LINES = None

#Don't check deviation after this hour
#Expected format: HH:MM:SS
LAST_TIME_TO_CHECK = ''

#Time to start again if you have stopped watching after a certain hour
#Expected format: HH:MM:SS
FIRST_TIME_TO_CHECK = ''

#Send email alerts
SEND_ALERT = False

#Receiver of the email alerts
ALERT_RECEIVER = ''

#Who should the alert be from
ALERT_SENDER = ''
