import re

txt=input()
pattern = "[A-Z]+[a-z]+$"

find = re.search(pattern, txt)
print(find)