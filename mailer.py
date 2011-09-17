# -*- coding: utf-8 -*-
import smtplib
import config
from email.mime.text import MIMEText

class Mailer:
  def __init__(self):
    self.sentDeviations = {}

  def sendDeviationResult(self,data):
    txt = self.createDeviationMsg(data)
    print txt
    if config.SEND_ALERT == False:
      return
    mailText = MIMEText(txt)
    mailText['To'] = config.ALERT_RECEIVER
    mailText['From']= config.ALERT_SENDER
    mailText['Subject'] = 'Deviation from SL!'
    s = smtplib.SMTP('localhost')
    s.sendmail(config.ALERT_SENDER,config.ALERT_RECEIVER,mailText.as_string())
    s.quit()

  def createDeviationMsg(self,data):
    txt = ''
    print 'SentDev len: '+str(len(self.sentDeviations))
    for deviation in data["GetDeviationsResponse"]["GetDeviationsResult"]["aWCFDeviation"]:
      if deviation['aDevCaseGid'] not in self.sentDeviations:
        txt+= deviation['aHeader'] + "\n"
        txt+= deviation['aDetails'] + "\n"
        txt+= deviation['aUpdated'] + "\n \n"
        self.sentDeviations[deviation['aDevCaseGid']] = deviation['aHeader']
    print 'SentDev len: '+ str(len(self.sentDeviations))
    return txt

