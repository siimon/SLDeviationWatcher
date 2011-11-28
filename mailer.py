# -*- coding: utf-8 -*-
import smtplib
import config
from email.mime.text import MIMEText

class Mailer:
  def sendDeviationResult(self,data):
    if data == None:
      return
    txt = self.createDeviationMsg(data)
    print txt
    if config.SEND_ALERT == False:
      return

    if len(txt) <= 0:
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
    for deviation in data:
        header = deviation['Header']
        details = deviation['Details']
        updated = deviation['Updated']
        
        if header != None and details != None and updated != None:
          txt+= deviation['Header'].encode('utf-8') + "\n"
          txt+= deviation['Details'].encode('utf-8') + "\n"
          txt+= deviation['Updated'].encode('utf-8') + "\n \n"
    return txt

