def mystring(str):
    lower=0
    upper=0
    for x in str:
        if x.isupper():
            upper+=1
        elif x.islower():
            lower+=1
        else:
            pass
    print(upper)
    print(lower)
            
s=input()
mystring(s)