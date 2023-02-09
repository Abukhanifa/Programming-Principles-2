class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f'Account owner: {self.owner}\nAccount balance: ${self.balance}'

    def deposit(self, dep_amt):
        self.balance += dep_amt
        print('Deposit Accepted')

    def withdraw(self, wd_amt):
        if self.balance >= wd_amt:
            self.balance -= wd_amt
            print('Withdrawal Accepted')
        else:
            print('Funds Unavailable!')

nm = str(input())
mn = int(input())
acc = Account(nm, mn)
E = False
while(E!=True):
    print (f"{acc.owner}, what would you like to do?")
    print("B=Check balance   D=Deposit    W=Withdrawal   E=Exit")
    ans = str(input())
    if(ans == "D"):
        print("How much would you like to deposit?")
        dep = int(input())
        acc.deposit(dep)
    elif(ans == "B"):
        print(f"Current balance is: {acc.balance}$")
    elif(ans == "W"):
        print("How much would you like to withdraw?")
        wit = int(input())
        acc.withdraw(wit)
    elif(ans == "E"):
        print("Have a nice day!")
        E = True
