import re
# Регулярные выражения
text = "" \
       "Привет! Отправь, пожалуйста, письмо " \
       "нашим коллегам vladamir@v.ru, vladimir2@v.ru;" \
       "про Оксану и Ольну незабудь: oksana@v.ru, olga@v.ru" \
       "" \
       "отошли копию партнерам: adidas@das.ru nike@ne.ki " \
       "Спасибо! " \
       "@@твой босс"

li = text.split()
print(li)

li = [n for n in li if "@" in n]
print(li)

re.findall("vlad.mir", text)
re.findall("\w+", text)
# \w+ - повторенный один или более раз символ буквы или цифры а также символ нижнего подчеркивания

print(re.findall("\w+@\w+\.\w+", text))