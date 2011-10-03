import MySQLdb
import config

class MySQLHelper:
  def __init__(self):
    self.db = MySQLdb.connect(config.MYSQL_HOST,config.MYSQL_USER,config.MYSQL_PASSWORD,config.MYSQL_DATABASE)
  def selectFromDB(self,query):
    cursor = self.db.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    return result;
  def selectSingleFromDB(self,query):
    cursor = self.db.cursor()
    cursor.execute(query)
    result = cursor.fetchone()
    return result[0]

  def executeOnTable(self,query):
    cursor = self.db.cursor()
    cursor.execute(query);
    self.commitAndClose()

  def commitAndClose(self):
    self.db.commit()
    self.db.close()
