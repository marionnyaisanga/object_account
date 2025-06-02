class Transactions:
    def __init__(self,amount,naration,account):
        self.date_and_time= datetime.now()
        self.amount=amount
        self.naration = naration
        self.account = account

    def show_transaction(self):
        return(f"{self.date_and_time} -{self.naration}:
        {self.account}")


class Account:
    def __init__(self,name):
        self.name = name
        self._balance = 0    
        self.deposits = []
        self.withdrawals = []
        self.loan = 0
        self.frozen = False
        self.minimum_balance = 0
        self.is_closed = False
        self.__account_number = account_number
        self.__transactions = []
    def set_balance(self,ammount):
        self._balance = amount
        

    def deposit(self, amount, narration="Deposit"):
        if amount > 0:
            transaction = Transaction(amount, narration, self)
            self.__transactions.append(transaction)
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount, narration="Withdrawal"):
        if amount > 0 and self.get_balance() >= amount:
            transaction = Transaction(-amount, narration, self)
            self.__transactions.append(transaction)
        else:
            print("Insufficient balance or invalid amount.")
    def get_transaction_history(self):
        return self.__transactions    
    def get_account_number(self):
        return self.__account_number
              
    def get_balance(self):
        return sum(transaction.amount for transaction in self.__transactions)

    def transfer_funds(self,amount):
        if amount > 0 and self.balance >= amount:
            self.withdrawals.append(amount)
            totalwithdrawal = 0
        for i in self.withdrawals:
            totalwithdrawal+=i

        totaldeposit = 0 
        for i in self.deposits:
            totaldeposit+=i

        self.balance = totaldeposit - totalwithdrawal 
        return f"Dear {self.name}, you transferd {amount}. Your new balance is {self.balance}"

    def request_loan (self,amount):
        if amount > 0 :
            self.loan +=amount
            return f"Your loan amount is {self.loan}"
    def repay_loan (self,amount):
        if amount > 0:
            self.loan -= amount
            self.balance -= amount
            return f"You have repaid your loan, your new loan debt is {self.loan}"        

    def account_details(self):
        return f"{self.name}, your balance is {self.balance}"

    def account_owner(self,newOwner):
        self.name = newOwner

    def account_statement(self):
        print("Account statement")
        for deposit in self.deposits:
            print(f"Deposit: {deposit}")
        for withdrawal in self.withdrawals:
            print(f"Withdrwal: {withdrawal}")   

    def min_balance(self, amount):
        if amount>=0:
            self.minimum_balance = amount
            return f"Your account minumum is {self.minimum_balance}"
        
    def apply_interest(self):
        interest = self.loan * 0.05
        self.loan += interest
        return f"Your interest is {interest} and total {self.loan}"
    def freeze(self):
        self.frozen = True
        return f"Account has been frozen for security reason"
    def un_freeze(self):
        self.frozen = False
        return f"Account has been unfrozen"
    def close_account(self):
        self.balance = 0
        self.deposits.clear()
        self.withdrawals.clear()
        self.loan = 0
        self.min_balance = 0
        return f"Your account has been closed"
    def print_account_summary(self):
        print(f"Account Number: {self.get_account_number()}")
        print(f"Current Balance: {self.get_balance()}")
        print("Transaction History:")
        for transaction in self.get_transaction_history():
            transaction.show_transaction()      

