class BankAccount:
    def __init__ (self,name,balance):
        self.name=name
        self.__balance=balance
        self.history=[]

    def __str__(self):
        return f"Name: {self.name} | Balence: ₹{self.__balance}"
    
    def __repr__(self):
        return f"Account(name={self.name}, Balence={self.__balance})"
    
    def save_transaction(self,type,amount,account_name=None):
        transaction={"type":type,"amount":amount,"account_name":account_name}
        self.history.append(transaction)
        
    @property
    def balance(self):
        return f"Your Balence:{self.__balance}"

    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
            print(f"Deposited {amount}. Balance: {self.__balance}")
            self.save_transaction("Deposit",amount)
        else:
            print("amount hsould be greater then 0")

    def withdraw(self,amount):
        if self.__balance>0:
            if amount>0:
                self.__balance-=amount
                print(f"Withdrawn {amount}. Balance: {self.__balance}")
                self.save_transaction("Withdraw",amount)
            else:
                print("amount should be greater then")
        else:
            print("insufficient balance")


    def transfer(self,account_name,amount):
        if self.__balance>0:
            if amount>0:
                self.__balance-=amount
                print(f"Transferred {amount} to {account_name}. Balance: {self.__balance}")
                self.save_transaction("Transfer",amount,account_name)
            else:
                print("amount should be greater then")
        else:
            print("insufficient balance")
    @property
    def transaction_history(self):
        print("Transaction History:")
        for index,transaction in enumerate(self.history,start=1):
            if not transaction["account_name"]:
                print(f"{index}. {transaction["type"]} {transaction["amount"]}")
            else :
                print(f"{index}. {transaction['type']} {transaction['amount']} to {transaction['account_name']}")


acc1=BankAccount("ajmal",100)
acc1.deposit(1000)
acc1.transfer("yasi",10)
print(acc1.balance)
acc1.transaction_history

