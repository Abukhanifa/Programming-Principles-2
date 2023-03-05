products = ["eggs", "bread", "meat", "bottle of water"]
file = open('list.txt', 'w')
for product in products:
    file.write(product+"\n")
