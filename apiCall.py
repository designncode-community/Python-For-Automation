import requests
import json
baseUrl = "http://krazycovidindia.azurewebsites.net/api/tracker"
paramter = {'city':'mumbai'}
response = requests.get(baseUrl,params=paramter)
formattedResponse = json.loads(response.content)
print(formattedResponse)