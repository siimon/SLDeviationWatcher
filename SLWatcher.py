# -*- coding: UTF-8 -*-

from datetime import datetime,timedelta
import sys
import SLApi
import config
import mailer
import time
import DeviationToDatabase
import pushover_client

class SLDeviationWatcher:
  def __init__(self):
    self.devMailer = mailer.Mailer()
    self.validateConfig()
    self.deviations = {}

  def run(self):
    nextCheck = datetime(2001,01,01,00,00,00,00)
    print "Next check: "+  str(nextCheck)

    while 1:
      for interval in config.INTERVAL_TIMES:
        start = self.convertStrToTime(interval['start'])
        stop = self.convertStrToTime(interval['stop'])
        now = datetime.now().time()

        if now >= start.time() and now <= stop.time() and nextCheck <= datetime.now():
          print 'Time to check deviation, time: '+str(datetime.now())
          self.checkDeviation()
          nextCheck = datetime.now() + timedelta(minutes=5)
          print 'Next check: '+ str(nextCheck)
          print "\n"

      time.sleep(20)

  def checkDeviation(self):
    lines = config.TRANSPORT_LINES
    transportMode = config.TRANSPORT_MODE
    api = SLApi.SLApi()
    s = None
    try:
      s = api.executeDeviationCall(lines,transportMode)
    except Exception,e:
      print 'Error checking deviation'
      print 'Exception: '+str(e)
    if s is not None:
     self.storeDeviations(s)
     self.sendDeviations(s)
  
  def sendDeviations(self,data):
    toSend = []
    for deviation in data:
      if deviation['Guid'] not in self.deviations:
        toSend.append(deviation)
        self.deviations[deviation['Guid']] = deviation['Header']
    try:
      self.devMailer.sendDeviationResult(toSend)
    except Exception,e:
      print 'Error sending alert'
      print 'Exception: '+str(e)

    try:
      self.sendPushNotice(toSend)
    except Exception, e:
      print 'Error sending push notice'
      print e
  
  def storeDeviations(self,data):
    try:
      if config.SAVE_DEVIATION is True:
        parser = DeviationToDatabase.DeviationToDatabase()
        for deviation in data:
          if deviation['Guid'] not in self.deviations:
           parser.parseMessage(deviation['Details'])

    except Exception,e:
      print 'Error parsing deviation'
      print str(e)

  def sendPushNotice(self, data):
    for deviation in data:
      print deviation['Main']
      if deviation['Main'] == 'true' or 'stopp vid' in deviation['Details']:
        pushover_client.send(deviation['Details'].encode('utf-8'))


  def validateConfig(self):
    print "Checking config. . . . . ."
    try:
      if len(config.INTERVAL_TIMES) <= 0:
        raise()
    except:
      self.printValidateError('Check INTERVAL_TIMES setting')

    try:
      if len(config.DEVIATION_API_KEY)<10:
       raise()
    except:
        self.printValidateError('Check DEVIATION_API_KEY setting')
    try:
      if config.TRANSPORT_MODE is None:
        raise()
    except:
      self.printValidateError('Check TRANSPORT_MODE setting')
    print 'Validation successfull!'

  def printValidateError(self,msg):
    print 'Validation of config failed.'
    print msg
    sys.exit()


  def convertStrToTime(self,inp):
    try:
      lastTime = time.strptime(inp,'%H:%M:%S')
      lastTimeToCheck = datetime(*lastTime[:6])
      return lastTimeToCheck
    except ValueError:
      print 'Error converting to datetime. Input: '+str(inp)
      return datetime.now()

if(__name__=="__main__"):
  devWatch = SLDeviationWatcher()
  devWatch.run()


