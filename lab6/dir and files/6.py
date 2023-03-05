import os, string

if not os.path.exists("directory"):
    os.makedirs("directory")
    
for file in string.ascii_uppercase:
    with open(file + ".txt", 'w') as f:
        f.writelines(file)
    
    