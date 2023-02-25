import re

txt=input()
rplc=re.sub(r"[ ,.]", ":", txt)
print(rplc)