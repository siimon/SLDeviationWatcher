import urllib
import datetime
import config
import json
class SLApi:
  deviationBaseURL = 'https://api.trafiklab.se/sl/storningsinfo/GetDeviations.json'

  def executeDeviationCall(self,lines,transportMode):
    today = datetime.date.today()
    if lines is not None:
      url = self.deviationBaseURL +'?key={0}&fromDate={1}&toDate={2}&lineNumber={3}&transportMode={4}'.format(config.DEVIATION_API_KEY,today,today,lines,transportMode)
    if lines is None:
      url = self.deviationBaseURL +'?key={0}&fromDate={1}&toDate={2}&transportMode={3}'.format(config.DEVIATION_API_KEY,today,today,transportMode)

    apiData = urllib.urlopen(url).read()
    jsonData = json.loads(apiData)
    result = self.mapDeviationResult(jsonData)
    return result

  def mapDeviationResult(self,response):
    result = []
    for deviation in  response["GetDeviationsResponse"]["GetDeviationsResult"]["aWCFDeviation"]:
      result.append({'Guid':deviation['aDevCaseGid'],'Header':deviation['aHeader'],'Details':deviation['aDetails'],'Updated':deviation['aUpdated'], 'Main': deviation['aMainNews']})
    return result
