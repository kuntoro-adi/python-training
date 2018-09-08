class BankAccount:
    def __init__(self, name, balance, type):
        self.name = name
        self.balance = balance 
        self.type = type
    def deposit(self, balance):
        self.balance += balance
    def withdraw(self, balance):
        if self.balance < balance:
            print('not enough money')
            return
        self.balance -= balance
    def transfer(self, account, balance):
        if self.type == 's' and balance > 5000000:
            print('exceed standard account limit')
            return
        account.deposit(balance)
        self.withdraw(balance)
    def print_info(self):
        print(self.name, self.balance, self.type)