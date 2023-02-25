def squares(N):
    for i in range (N):
        yield i**2
        
n = int(input())
for x in squares(n):
    print(x)