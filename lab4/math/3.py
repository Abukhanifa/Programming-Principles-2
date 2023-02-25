import math

def polygon(s=int(input()), l=int(input())):
    print("Input number of sides:", s)
    print("Input the length of a side:", l)
    area = (s * l**2) / (4 * math.tan(math.pi/s))
    print("The area of the polygon is:", area)
    
polygon()
