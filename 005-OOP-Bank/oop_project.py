from bank_accounts import *

Bharath = BankAccount(1000, 'bharath')
john = BankAccount(2000, 'john')


Bharath.get_balance()
john.get_balance()


Bharath.deposit(500)
Bharath.withdraw(100)
Bharath.transfer(10, john)


jim = InterestRewardAcct(1000, 'jim')
jim.get_balance()
jim.deposit(100)
jim.transfer(100, Bharath)


blaze = SaavingsAcct(1000, 'blaze')
blaze.get_balance()
blaze.deposit(100)
blaze.transfer(1000, john)