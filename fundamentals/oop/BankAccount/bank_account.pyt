class BankAccount:

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        if self.balance < amount:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Balance {self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self

account1 = BankAccount(balance=300, int_rate=0.5)
account2 = BankAccount(balance=700, int_rate=1.3)


account1.deposit(10).deposit(30).deposit(50).withdraw(80).yield_interest().display_account_info()
account2.deposit(50).deposit(50).withdraw(5).withdraw(50).withdraw(20).withdraw(35).yield_interest().display_account_info()