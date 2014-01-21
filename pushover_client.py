# -*- coding: UTF-8 -*-
import config
import urllib2

def send(msg):
  if not config.PUSHOVER_SEND_PUSH_NOTIFICATIONS:
    return

  try:
    s = 'token={0}&user={1}&message={2}'.format(config.PUSHOVER_APP_KEY, config.PUSHOVER_USER_KEY, msg)
    req = urllib2.Request('https://api.pushover.net/1/messages.json', s)
    urllib2.urlopen(req)
  except Exception,e:
    print e


