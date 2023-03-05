import math

n = int(input())
a = list(map(int,input().strip().split()))[:n]
prod=math.prod(a)
print(prod)