
class Account:
    def __init__(self,name):
        self.name = name
        self.balance = 0
        self.deposits =[]
        self.withdrawals = []
        self.loan = 0
        self.frozen = False
        self.minimum_balance = 0
        self.is_closed = False

    def deposit(self,amount):
        if amount>0:
            self.deposits.append(amount)
        totaldeposit = 0
        for i in self.deposits:
            totaldeposit+=i
        self.balance+=totaldeposit
        
        return f"Dear {self.name} your balance is {totaldeposit}"

    def withdrawals(self,amounts):
        if accounts > 0 and (self.balance - amount) >= self.minimum_balance:
            self.withdrawals.append(amounts)
            self.balance = self.balance - amounts
            return f"Dear {self.name} your new balance is {self.balance})"


    def transfer_funds(self, account):
        if amount > 0 and self.balance >= amount:
            self.withdrawals.append(amount)
            totalwithdrawal = 0
        for i in self.withdrawals:
            totalwithdrawal+=i

        self.balance = totaldeposit - totalwithdrawal
        return f"Dear {self.name}, you have transfered{amount}, new balance is {self.balance}"
    def request_loan (self,amount):
        if amount > 0 :
            self.loan += amount
            return f" Your loan is{self.loan}"


    def repay_loan(self,amount):
        if amount > 0:
            self.loan -= amount
            self.balance -= account
            return f" you have paid your loan, new loan is{s}"

    def balance (self):
        return f" Dear {self.name}, your balance is{self.balance}"

    def account_owner(self,new_name):
        self.name = new_name
    
    def account_statement(self):
        for deposit in self.deposits:
            print(f"Deposit: {deposits}")
        for withdrawal in self,withdrawals:
            print(f"Withdrawal: {withdrawal}")

    def min_balance(self,amount):
        if ammount>=0:
            self.minimum_balance = amount
            return f" Your minimum account is {self.min_balance}"
    
    def apply_for_interest(self):
        interest = self.loan * 0.05
        self.loan += interest
        return f"Your interest is {interest} total {self.loan}"

    def freeze(self):
        self.frozen = True
        return f"Account has been frozen"
    def un_freeze(self):
        self.frozen = False
        return f" Account is unfrozen"
    
    def close_account(self):
        self.balance = 0
        self.deposits.clear()
        self.withdrawals.clear()
        self loan = 0
        self.min_balance = 0
        return f" Your account has been closed"



