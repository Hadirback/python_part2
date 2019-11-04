import re

with open('weather.html', 'r', encoding='UTF-8') as f:
    s = f.read()

li = re.findall('<a class="home-link home-link_black_yes weather__grade" aria-label="([^"]+)" href="', s)
print(li)