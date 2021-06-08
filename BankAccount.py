class BankAccount:
    bank_name = "First National Dojo"
    all_accounts = [] 
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
        
    def deposit(self, amount):
        self.balance+= amount
        return self
    def withdraw(self, amount):
        self.balance-=amount
        return self
    def display_account_info(self):
        print(self.balance)
        return self
    def yield_interest(self):
        if self.balance>0:
            temp = self.balance
            temp*=(self.int_rate/100)
            self.balance+=temp
        return self
    @classmethod
    def allAccounts(cls):
        for acct in cls.all_accounts:
            print(f"{acct.balance} and {acct.int_rate}")


my_account = BankAccount(0.5,200)
jacobs_account = BankAccount(0.5,2000)
my_account.deposit(100).deposit(200).deposit(300).withdraw(200).yield_interest().display_account_info()
jacobs_account.deposit(100).deposit(1000).withdraw(300).withdraw(200).withdraw(100).withdraw(50).yield_interest().display_account_info()
BankAccount.allAccounts()