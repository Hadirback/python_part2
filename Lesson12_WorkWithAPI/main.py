import requests
import json
site = 'https://samples.openweathermap.org/data/2.5/weather?q=London,uk&appid=b6907d289e10d714a6e88b30761fae22'

resp = requests.get(site)
text_page = resp.text

print(text_page)

data = json.loads(text_page)
print(data['main']['temp'] - 273)

