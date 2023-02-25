def iterate(n):
    for i in range(n):
        if i!=0 and i%3==0 and i%4==0:
            yield i
            
a=int(input())
for x in iterate(a):
    print(x)
