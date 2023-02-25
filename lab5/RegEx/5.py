import re

txt = input()
pattern = "a.*?b$"

src = re.search(pattern, txt)
print(src)