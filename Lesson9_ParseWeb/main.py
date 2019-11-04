import re

with open('rbk.html', 'r', encoding='UTF-8') as f:
    s = f.read()

comment = re.compile("<!--.*?-->", re.DOTALL)
script = re.compile("<script.*?/script>", re.DOTALL)
tags = re.compile("<[^>]*>")
s = comment.sub("", s)
s = script.sub("", s)
s = tags.sub("", s)
s = re.sub("[ ]+", " ", s)
s = re.sub("\s{2,}", "\n", s)
print(s)