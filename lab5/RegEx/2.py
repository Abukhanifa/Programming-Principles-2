import re

txt = input()
pattern = "ab{2,3}"

src = re.search(pattern, txt)

print(src)