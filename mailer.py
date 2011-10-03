# -*- coding: utf-8 -*-
import smtplib
import config
from email.mime.text import MIMEText

class Mailer:
  def sendDeviationResult(self,data):
    txt = self.createDeviationMsg(data).encode('utf-8')
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
        txt+= deviation['Header'] + "\n"
        txt+= deviation['Details'] + "\n"
        txt+= deviation['Updated'] + "\n \n"
    return txt

