# compile

# re compile - если нужно найти и изменить что то подходящее под
# шаблон в нескольких переменных

import re

text1 = """
Сбо́рная Франции по футбо́лу 34-я минута представляет Францию в международных 
матчах и турнирах по футболу. """

text2 = """
Управляющая организация 56-й номер — Федерация футбола Франции.
"""
text3 = """
Федерация является членом ФИФА с 1904 года, членом УЕФА с 1954 
года. Французы 1-й час были одними из основателей обеих этих организаций. 
"""

# вытаскиваем из всех текстов минуты
pattern_string = "\d{1,2}\-[йя]"
print(re.findall(pattern_string, text1))
print(re.findall(pattern_string, text2))
print(re.findall(pattern_string, text3))

# pattern_string  постоянно преобразуется к паттерну что
# достаточно трудоемкая задача

pattern = re.compile("\d{1,2}\-[йя]")
print(type(pattern))
print(pattern.findall(text2))
print(pattern.findall(text1))
print(pattern.findall(text3))

print(re.sub(pattern, "n", text3))
# compile выполняется быстрее

