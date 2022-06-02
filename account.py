class Account:
    accounttype="saving account"
    def __init__(self,pin,balance,accnumber,username,deposit,withdraw):
        self.balance=balance
        self.pin=pin
        self.accnumber=accnumber
        self.username=username
        
    def deposit(self, deposit):
     self.balance+=deposit
     return self.balance
    def withdraw(self,withdraw):
        self.balance-=withdraw
        return self.balance
    
