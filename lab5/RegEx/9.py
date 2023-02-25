import re

txt = input()

ins = re.sub(r"(\w)([A-Z])", r"\1 \2", txt)
print(ins)


