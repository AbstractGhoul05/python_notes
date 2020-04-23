class Account:
    
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, deposit_val):
        self.balance += deposit_val
        print("Deposit Accepted")

    def withdraw(self, draw_val):
        if draw_val > self.balance:
            print("Funds Unavailable!")
            return
        else:
            self.balance -= draw_val
            print("Withdrawal Accepted")

    def __str__(self):
        return f"Account owner:    {self.owner}\nAccount balance:  ${self.balance}"

acct1 = Account('AbstractGhoul05', 100)
print(acct1)
print(acct1.owner)
print(acct1.balance)
acct1.deposit(50)
acct1.withdraw(75)
acct1.withdraw(500)
