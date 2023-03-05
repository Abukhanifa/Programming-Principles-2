import os
path="C:\\Users\\User\\Desktop\\pp2\\lab6\\dir and files\\example.txt"
if os.path.exists(path):
    os.remove("example.txt")
else:
    print("The File does not exist")