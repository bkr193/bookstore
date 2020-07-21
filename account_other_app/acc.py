class Account:

    def __init__(self, file):
        self.file = file
        with open(file, 'r') as f:
            self.balance = int(f.read())

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def commit(self):
        with open(self.file, 'w') as f:
            f.write(str(self.balance))


class Checking(Account):

    def __init__(self, file, fee):
        Account.__init__(self, file)
        self.fee = fee

    def transfer(self, amount):
        self.balance = self.balance - amount - self.fee


check = Checking('balance.txt', 1)
check.transfer(10)
print(check.balance)
check.commit()
