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
    return jsonData
