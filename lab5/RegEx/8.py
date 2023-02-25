import re

txt=input()
pattern=r"[A-Z][^A-Z]*"

omg = re.findall(pattern, txt)
print(omg)