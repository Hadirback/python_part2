# изменение текста с помощью регулярных выражений
import re

text = """
Сбо́рная Франции по футбо́лу представляет Францию в международных 
матчах и турнирах по футболу. Управляющая организация — Федерация 
футбола Франции. Федерация является членом ФИФА с 1904 года, членом 
УЕФА с 1954 года. Французы были одними из основателей обеих этих 
организаций. на 23-й минуте на 35-я минута
"""

text = re.sub("[Фф]ранцузы", "Россияне", text)
text = re.sub("Франц", "Росс", text)

text = re.sub("\d{1,2}\-[й,я]", "n", text)

print(text)