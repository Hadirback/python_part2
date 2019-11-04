import re
from bs4 import BeautifulSoup as BS

with open('rbk.html', 'r', encoding='UTF-8') as f:
    s = f.read()

soup = BS(s, "html.parser")
# print(soup.prettify())
# print(soup.get_text())
print(soup.title.string)
# print(soup.div)
print(soup.div['class'])
# print(soup.find_all("div"))
print(len(soup.find_all("div")))

link_example = """<a href="LINK">CONTENT</a>"""
li = soup.find_all("a")
for n in li:
    print(n.get("href", ""))
