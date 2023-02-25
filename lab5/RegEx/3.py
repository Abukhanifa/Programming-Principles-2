import re

txt = input()
pattern = "^[a-z]+_[a-z]+$"

src = re.search(pattern, txt)
print(src)