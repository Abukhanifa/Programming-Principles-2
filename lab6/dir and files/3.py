import os
print("Test a path exists or not:")
path1 = r'C:\Users\User\Desktop\pp2\lab6\dir and files\file.txt'
print(os.path.exists(path1))
path1 = r'C:\Users\User\Desktop\pp2\lab6\dir and files\file.txt'
print(os.path.exists(path1))
print("File name of the path:")
print(os.path.basename(path1))
print("Dir name of the path:")
print(os.path.dirname(path1))