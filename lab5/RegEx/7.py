import re

txt = input()
pattern=''.join(x.capitalize() or '_' for x in txt.split('_'))
print(pattern)