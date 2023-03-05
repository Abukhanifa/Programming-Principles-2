str = input()
str= str.casefold()
reverse = reversed(str)
if list(str) == list(reverse):
   print("Palindrome")
else:
   print("Not Palindrome")