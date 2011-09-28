# -*- coding: UTF-8 -*-
import config
from datetime import datetime
import mysql

class DeviationToDatabase:
  def parseMessage(self,msg):
    parts = msg.encode('utf-8').split('på grund av')
    reason = parts[len(parts) - 1]
    print 'Reason: '+reason

  def insertDeviation(self,deviation):
    sql = 'INSERT INTO Deviation(Reason,DeviationTime) VALUES('+deviation+','+datetime.today()+')'
    m = mysql.MySQLHelper()
    m.executeOnTable(sql)
