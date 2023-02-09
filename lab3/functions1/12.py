def histogram(h):
    for i in range(0,len(h)):
        print(h[i]*'*')

h=[]
num=int(input())
for i in range(0,num):
    el=int(input())
    h.append(el)
    
    
histogram(h)