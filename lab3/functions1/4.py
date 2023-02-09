def is_prime(num):
    if num == 2:
        return True
    for i in range(2, num):
        if num%i==0:
            return False
        return True
    
list1=[]

num=int(input())

for i in range(0,num):
    el=int(input())
    list1.append(el)
    
for i in range(1,10):
    prime_list = list(filter(lambda x: (is_prime(x) == True), list1))
print(prime_list)
    

