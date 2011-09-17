# -*- coding: UTF-8 -*-
from datetime import datetime,timedelta
import sys
import SLApi
import config
import mailer
import time

class SLDeviationWatcher:
  def __init__(self):
    self.devMailer = mailer.Mailer()
    self.validateConfig()

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

  def checkDeviation(self):
    lines = config.TRANSPORT_LINES
    transportMode = config.TRANSPORT_MODE
    api = SLApi.SLApi()
    try:
      s = api.executeDeviationCall(lines,transportMode)
      #s = {"GetDeviationsResponse":{"@xmlns":"http:\/\/tempuri.org\/","GetDeviationsResult":{"@xmlnsa":"http:\/\/schemas.datacontract.org\/2004\/07\/SLTAWCF","@xmlnsi":"http:\/\/www.w3.org\/2001\/XMLSchema-instance","aWCFDeviation":[{"aLink":"http:\/\/storningsinformation.sl.se\/?DMVID=4050000129821863","aCreated":"2011-09-02T09:01:04.64","aMainNews":"false","aSortOrder":1,"aHeader":"HÃ¥llplats Jungfrugatan flyttad","aDetails":"HÃ¥llplats Jungfrugatan Ã¤r flyttad 45 meter abakÃ¥t fÃ¶r blÃ¥buss 1 mot Stora Essingen och 4 mot Gullmarsplan och buss 62 mot FredhÃ¤ll, 72 mot Karlbergs station, 91 mot Frihamnen och 94 mot Gullmarsplan frÃ¥n och med 2011-09-07 pÃ¥ grund av vÃ¤garbete.\nDetta planeras pÃ¥gÃ¥ till och med 2011-09-14.","aScope":"Buss 62, 72, 91, 94, blÃ¥buss 1, 4","aDevCaseGid":4050000129821856,"aDevMessageVersionNumber":1,"aScopeElements":"Buss 62, 72, 91, 94, blÃ¥buss 1, 4","aMobileLink":"http:\/\/mobil.sl.se\/ext\/mobilta1.sl.se\/DeviationList.aspx\/DeviationList.aspx?MessageID=4050000129821863","aFromDateTime":"2011-09-07T05:00:00","aUpToDateTime":"2011-09-14T23:30:00","aUpdated":"2011-09-02T09:01:04.64","aInternalNote":"null"},{"aLink":"http:\/\/storningsinformation.sl.se\/?DMVID=4050000128927389","aCreated":"2011-08-29T14:50:02.28","aMainNews":"false","aSortOrder":2,"aHeader":"HÃ¥llplats RÃ¶kubbsgatan flyttad","aDetails":"HÃ¥llplats RÃ¶kubbsgatan Ã¤r flyttad 75 meter bakÃ¥t fÃ¶r blÃ¥buss 1 mot Stora Essingen och buss 91 mot Stora Essingen frÃ¥n och med 2011-09-02 pÃ¥ grund av vÃ¤garbete.\nDetta planeras pÃ¥gÃ¥ till och med 2011-10-31.","aScope":"Buss 91, blÃ¥buss 1","aDevCaseGid":4050000128927386,"aDevMessageVersionNumber":2,"aScopeElements":"Buss 91, blÃ¥buss 1","aMobileLink":"http:\/\/mobil.sl.se\/ext\/mobilta1.sl.se\/DeviationList.aspx\/DeviationList.aspx?MessageID=4050000128927389","aFromDateTime":"2011-09-02T05:00:00","aUpToDateTime":"2011-10-31T23:30:00","aUpdated":"2011-08-29T14:50:02.28","aInternalNote":"null"},{"aLink":"http:\/\/storningsinformation.sl.se\/?DMVID=4050000128927245","aCreated":"2011-08-29T14:49:23.367","aMainNews":"false","aSortOrder":3,"aHeader":"HÃ¥llplats Sandhamnsplan flyttad","aDetails":"HÃ¥llplats Sandhamnsplan Ã¤r flyttad till TegeluddsvÃ¤gen fÃ¶r blÃ¥buss 1 mot Stora Essingen och buss 91 mot Stora Essingen frÃ¥n och med 2011-09-02 pÃ¥ grund av vÃ¤garbete.\nDetta planeras pÃ¥gÃ¥ till och med 2011-10-31.","aScope":"Buss 91, blÃ¥buss 1","aDevCaseGid":4050000128927242,"aDevMessageVersionNumber":2,"aScopeElements":"Buss 91, blÃ¥buss 1","aMobileLink":"http:\/\/mobil.sl.se\/ext\/mobilta1.sl.se\/DeviationList.aspx\/DeviationList.aspx?MessageID=4050000128927245","aFromDateTime":"2011-09-02T05:00:00","aUpToDateTime":"2011-10-31T23:30:00","aUpdated":"2011-08-29T14:49:23.367","aInternalNote":"null"}]}}}
      self.devMailer.sendDeviationResult(s)
    except:
      print 'Error checking deviation'

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

  def printValidateError(self,msg):
    print 'Validation of config failed.'
    print msg
    sys.exit()


  def convertStrToTime(self,inp):
    try:
      lastTime = time.strptime(config.LAST_TIME_TO_CHECK,'%H:%M:%S')
      lastTimeToCheck = datetime(*lastTime[:6])
      return lastTimeToCheck
    except ValueError:
      print 'Error converting to datetime. Input: '+str(inp)
      return datetime.now()

if(__name__=="__main__"):
  devWatch = SLDeviationWatcher()
  devWatch.run()


