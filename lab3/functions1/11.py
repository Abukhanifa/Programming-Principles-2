def is_palindrome(s):
    return s==s[::-1]

string=str(input())

if is_palindrome(string):
    print("Palindrome")
else:
    print("Not Palindrome")
    