with open(r"file.txt", 'r') as f:
    lines = len(f.readlines())
    print('Total Number of lines:', lines)