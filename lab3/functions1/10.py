def unique_list(l):
    list=[]
    for x in l:
      if x not in list:
        list.append(x)
    return list
        
        
list1=[]

num=int(input())

for i in range(0,num):
    el=int(input())
    list1.append(el)
    
print(unique_list(list1))

    