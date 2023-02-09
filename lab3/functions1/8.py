def spy_game(nums):
    for i in range(0,len(nums)-1):
        if nums[i]==0 and nums[i+1]==0 and nums[i+2]==7:
            print("True")
            return True
    print("False")
    return False

list=[]

num=int(input())

for i in range(0,num):
    el=int(input())
    list.append(el)
    
spy_game(list)