def has_33(nums):
    for i in range(0, len(nums)-1):
        if nums[i:i+2] == [3,3]:
            print("True")
            return True
    print("False")
    return False
        
list=[]

num=int(input())

for i in range(0,num):
    el=int(input())
    list.append(el)
    
has_33(list)

         
    