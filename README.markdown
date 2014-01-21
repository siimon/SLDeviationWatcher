##Deviation tracker for SL (Stockholm commuter traffic)

This project tracks deviations from SL (Stockholms Länstrafik).

When a new deviation has been detected, an email is sent to configured user and if the deviation is a major distruption a push notice is sent through [Pushover](http://pushover.net)

### Requirements:
* Local running smtp server
* Only tested on Python 2.7, might work on other versions aswell..
* An API Key for SLDeviationAPI from traiklab.se (free, though a registered project is required)

### Other features:
* Possible to store each deviation, with reason and time.
* Pushnotifications through Pushover

### Setup instructions
Copy default_config.py and rename it to config.py
Change desired configurations in config.py to match your environment.

run python SLWatcher.py
