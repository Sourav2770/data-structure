class BankAccount:

    def __init__(self,name,initial_balance = 0):
        self.name = name
        self.balance = initial_balance



    def deposit(self, amount):
        if amount >= 0:
            self.balance += amount

        else:
            print(f"Amount must be positive")    
    

    def withdraw(self,amount):

        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Current Balance after withdrawal of {amount} rupees is {self.balance}")

            else:
                print(f"Insufficient Balance")

        else:
            print("Amount must me positive")        


    def current_balance(self):
        print(f"Current balance of {self.name}'s account is {self.balance}") 




account1 = BankAccount("Safa",1000)

account1.deposit(2000)

account1.withdraw(500)

account1.current_balance()
