import re

txt = input()
a=re.sub('([a-z0-9])([A-Z])', r'\1_\2', txt).lower()
print(a)
