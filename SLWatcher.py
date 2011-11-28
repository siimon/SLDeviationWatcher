# -*- coding: UTF-8 -*-
from datetime import datetime,timedelta
import sys
import SLApi
import config
import mailer
import time
import DeviationToDatabase

class SLDeviationWatcher:
  def __init__(self):
    self.devMailer = mailer.Mailer()
    self.validateConfig()
    self.deviations = {}

  def run(self):
    nextCheck = datetime(2001,01,01,00,00,00,00)
    print "Next check: "+  str(nextCheck)

    while 1:
      lastTimeToCheck = self.convertStrToTime(config.LAST_TIME_TO_CHECK)


      if nextCheck.time() > lastTimeToCheck.time():
        dateTomorrow = datetime.now() + timedelta(days=1)
        nextTime = self.convertStrToTime(config.FIRST_TIME_TO_CHECK)
        nextCheck = datetime(dateTomorrow.year,dateTomorrow.month,dateTomorrow.day,nextTime.hour,nextTime.minute,nextTime.second)
        print 'Max time for today reached, next check is: '+str(nextCheck)

      if nextCheck <= datetime.now():
        print 'Time to check deviation, time: '+str(datetime.now())
        self.checkDeviation()
        nextCheck = datetime.now() + timedelta(minutes=5)
        print 'Next check: '+ str(nextCheck)
        print "\n \n \n"

      time.sleep(20)

  def checkDeviation(self):
    lines = config.TRANSPORT_LINES
    transportMode = config.TRANSPORT_MODE
    api = SLApi.SLApi()
    try:
      s = api.executeDeviationCall(lines,transportMode)
    except Exception,e:
      print 'Error checking deviation'
      print 'Exception: '+str(e)
    if s is not None:
     self.storeDeviations(s)
     self.sendDeviations(s)
  
  def sendDeviations(self,data):
    try:
      toSend = []
      for deviation in data:
        if deviation['Guid'] not in self.deviations:
          toSend.append(deviation)
          self.deviations[deviation['Guid']] = deviation['Header']

      self.devMailer.sendDeviationResult(toSend)
    except Exception,e:
      print 'Error sending alert'
      print 'Exception: '+str(e)
  
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

  def validateConfig(self):
    print "Checking config. . . . . ."
    try:
      if config.LAST_TIME_TO_CHECK is not None and config.FIRST_TIME_TO_CHECK is not None:
        t = time.strptime(config.LAST_TIME_TO_CHECK,'%H:%M:%S')
        t2 = time.strptime(config.FIRST_TIME_TO_CHECK,'%H:%M:%S')
    except:
      self.printValidateError('Check LAST_TIME_TO_CHECK and FIRST_TIME_TO_CHECK')
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


