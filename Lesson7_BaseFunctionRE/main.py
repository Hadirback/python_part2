# re.search
# re.match
# re.split

import re

text = """Сборная Франции по футбо́лу представляет Францию в международных 
матчах и турнирах по футболу. Управляющая организация — Федерация 
футбола Франции. Федерация является членом ФИФА с 1904 года, 
членом УЕФА с 1954 года. Французы были одними из основателей 
обеих этих организаций. 
"""

pattern1 = "Франции"
pattern2 = "России"

re.search(pattern1, text)
print(re.search(pattern1, text).group())
print(re.match("Сборная", text))
# match - ищет первое слово в тексте

# split - разделение строки

print(re.split("по", text))
