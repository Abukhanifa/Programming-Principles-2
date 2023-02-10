#1
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

#2
def my_function(grams=int(input())):
    ounces=grams*28.3495231;
    print(ounces)
    
my_function ()

#3
def reversed_string(s=str(input())):
    a=s.split()
    a.reverse()
    print(' '.join(a))
    
#4

def is_palindrome(s):
    return s==s[::-1]

string=str(input())

if is_palindrome(string):
    print("Palindrome")
else:
    print("Not Palindrome")
    