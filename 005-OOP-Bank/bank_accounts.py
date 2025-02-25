class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, initialAmount, acctName):
        self.balance = initialAmount
        self.name = acctName
        print(f"\n account '{self.name}' created. \n Balance = ${self.balance:.2f}")

    def get_balance(self):
        print(f"\n Account '{self.name}' balance = ${self.balance:.2f}")
    def deposit(self, amount):
        self.balance = self.balance + amount
        print("\nDeposit Complete!")
        self.get_balance()

    def viableTransaction(self, amount):
        if self.balance >= amount:
            return 
        else: 
            raise BalanceException(
                f"\nSorry, account '{self.name}' only has a balance of ${self.balance:.2f}"
            )

    def withdraw(self, amount):
        try: 
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print('\nWithdraw Complete!')
            self.get_balance()
        except BalanceException as error: 
            print(f'\n withdraw interupter: {error}')


    def transfer(self, amount, account):
        try: 
            print('\n**********\n\nBeginning Transfer...')
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print('\nTransfer Complete!')
            print('\n**********')
        except BalanceException as error:
            print(f'\n transfer interrupted. {error}')



class InterestRewardAcct(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance+ (amount * 1.05)
        print("\n Deposit Complete.")
        self.get_balance()


class SaavingsAcct(InterestRewardAcct):
    def __init__(self, initialAmount, acctName):
        super().__init__(initialAmount, acctName)
        self.fee = 5
    def withdraw(self, amount):
        try: 
            self.viableTransaction(amount+self.fee)
            self.balance=self.balance-(amount+self.fee)
            print("\n withdraw complplete. $5 fee")
        except BalanceException as error:
            print(f'\nWithdraw interuppted : {error}')