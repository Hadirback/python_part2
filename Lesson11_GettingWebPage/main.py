import requests
import re

req = requests.get("https://yandex.ru")

print(req)

page_text = req.text
print(page_text)

li = re.findall('[0-9-+]+ °C', page_text)

print(li)