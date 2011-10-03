# -*- coding: UTF-8 -*-
import config
from datetime import datetime
import mysql

class DeviationToDatabase:
  def parseMessage(self,msg):
    parts = msg.encode('utf-8').split('på grund av')
    reason = parts[len(parts) - 1]
    self.insertDeviation(reason)

  def insertDeviation(self,deviation):
    now = datetime.now()
    sql = 'INSERT INTO Deviation(Reason,DeviationTime) VALUES(\''+deviation+'\',\''+ now.strftime("%Y-%m-%d %H:%M:%S") +'\')'
    m = mysql.MySQLHelper()
    m.executeOnTable(sql)
