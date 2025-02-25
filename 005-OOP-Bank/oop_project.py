from bank_accounts import *

Bharath = BankAccount(1000, 'bharath')
john = BankAccount(2000, 'john')


Bharath.get_balance()
john.get_balance()


Bharath.deposit(500)


Bharath.withdraw(100)


Bharath.transfer(10, john)