from datetime import datetime
class Account:
    accounttype="saving account"
    def __init__(self,accnumber,username):
        self.balance=0
        self.accnumber=accnumber
        self.username=username
        self.deposits=[]
        self.withdrawals=[]
        self.transaction=[]
        self.date=datetime.now()
        self.loan_balance=0
        
    def deposit(self,amount):
     self.balance+=amount
     return f"You have deposited {amount}. Your new balance is {self.balance}"

    def deposit(self,amount):
       if amount<=0:
        return f"Deposits amount should be more than zero"

       self.balance+=amount
       self.deposits.append({"date":self.date.strftime("%c"),"amount":amount,"narration":"deposit"})
       return f"You have deposited {amount}. Your new balance is {self.balance}"
 
    def withdraw(self,amount):
        if amount>self.balance:
         return f"Your balance is {self.balance}. You cannot withdraw the {amount}"

        elif amount<0:
            return f"Amount must be greater than 0"

        else:
            self.transaction=100
            self.balance-=amount + self.transaction 
            self.withdrawals.append({"date":self.date.strftime("%c"),"amount":amount,"narration":"withdraw"})
            return f"You have withdrawn {amount}. Your new balance is {self.balance}"
            

    def deposits_statement(self):
        for x in self.deposits:
            print(x)
    
    def withdrawals_statement(self):
        for x in self.withdrawals:
            print(x)
    def show_current_balance(self):
        balance=self.balance
        return f"Your current balance is {balance}"
    
    def full_statement(self):
        statements=self.withdraw+self.deposits
        for stmt in statements:
            print(stmt)
    
    def borrow(self,amount):
        deposit_history=sum(self.deposits)
        qualification=deposit_history*1/3
        interest=0.03*amount
        if amount <0:
            print("Amount must be positive")
        elif len(self.deposit)<10:
             print("You must have atleast 10 deposits ")
        elif amount <100:
            print("Loan request must be more than 100")
        elif amount>=qualification:
            print("You cannot borrow more than the qualification history")
        elif self.loan_balance >0:
            print("Clear your previous loan balance of {self.loan_balance}")
        else:
            self.loan_balance+=interest
            print(f"You have borrowed a loan of{amount} and your interest is {interest}. Your total payment will be {self.loan_balance}")
        
    def loan_repayment(self,amount):
        
            self.loan_balance-=amount
            print(f'you have paid {amount} and your loan balance is {self.loan_balance}')
        
            

        
    
        
    


    
    
