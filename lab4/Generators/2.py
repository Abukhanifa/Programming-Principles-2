def even(n):
    for i in range(n):
        if i%2 == 0:
            yield i
        i+=1
        
n=int(input())
values = []
for i in even(n):
    values.append(str(i))

print (",".join(values))