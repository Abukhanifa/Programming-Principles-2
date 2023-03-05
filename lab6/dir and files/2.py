import os
print('Exist:', os.access('C:\\Users\\User\\Desktop\\pp2\\lab6\\dir and files\\file.txt', os.F_OK))
print('Readable:', os.access('C:\\Users\\User\\Desktop\\pp2\\lab6\\dir and files\\file.txt', os.R_OK))
print('Writable:', os.access('C:\\Users\\User\\Desktop\\pp2\\lab6\\dir and files\\file.txt', os.W_OK))
print('Executable:', os.access('C:\\Users\\User\\Desktop\\pp2\\lab6\\dir and files\\file.txt', os.X_OK))