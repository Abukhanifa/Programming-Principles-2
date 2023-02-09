import random

print("Hello! What is your name?")
name=input()
rand1=random.randint(1,20)
print(f"Well, {name}, I am thinking of a number between 1 and 20.")
ans = int(100)
guess = 1
while ans != rand1:
    print("Take a guess")
    ans=int(input())
    if ans > rand1:
        print("Your guess is too high.")
        guess += 1
    elif ans < rand1:
        print("Your guess is too low")
        guess += 1
    elif ans == rand1:
        print(f"Good job, {name} You guessed my number in {guess} guesses!")