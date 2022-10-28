print("Welcome to Python Bank \n")


class Account:
    def __init__(self, owner, balance=0):
        self.owner = input("Kindly, Enter your name: ")
        self.balance = balance

    def deposit(self, deposit_amt):
        self.balance += deposit_amt
        print(f"You deposited {deposit_amt} to the Python. \nYour new Balance is {self.balance}")

    def withdrawn(self, withdrawn_amt):
        if self.balance >= withdrawn_amt:
            self.balance -= withdrawn_amt
            print("Withdrawal accepted")

        else:
            print("Sorry, you don't have enough funds to perform this transaction \nKindly, deposit funds!")

    def __str__(self):
        return f"Owner: {self.owner} \nBalance: {self.balance}"


a = Account(500)
print(a)
print("------------")
a.deposit(100)
print(a)
print("------------")
a.withdrawn(700)
print(a)
print("------------")
a.withdrawn(600)
print(a)