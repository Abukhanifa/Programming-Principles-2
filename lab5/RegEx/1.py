import re

txt = input()
pattern = ".*ab"

src = re.search(pattern, txt)

print(src)