import os
with open("firstcopy.txt", "r") as first, open("secondcopy.txt", "w") as second:

 for line in first:
     second.write(line)