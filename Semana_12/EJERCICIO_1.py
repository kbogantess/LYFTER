"""1. Cree una clase de `BankAccount` que:

    1. Tenga un atributo de `balance`.
    2. Tenga un método para ingresar dinero.
    3. Tengo un método para retirar dinero.
    
    Cree otra clase que herede de esta llamada `SavingsAccount` que:
    
    1. Tenga un atributo de `min_balance` que se pueda asignar al crearla.
    2. Arroje un error si se intenta retirar dinero y el `balance` está debajo del `min_balance`."""



class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance  

    def add_money(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"You have deposited {amount} into your account; Current balance: {self.balance}")
        else:
            print("You must enter a valid amount")

    def take_out_money(self, amount):
        if amount <= 0:
            print("You must select a valid amount")
        elif amount > self.balance:
            print("You do not have enough balance to make the withdrawal")
        else:
            self.balance -= amount
            print(f"You have withdrawn {amount}; Remaining balance: {self.balance}")

class SavingsAccount(BankAccount):
    def __init__(self, balance, min_balance):
        super().__init__(balance)  
        self.min_balance = min_balance   

    def take_out_money(self, amount):
        if self.balance - amount < self.min_balance:
            print(f"You cannot withdraw money. The minimum balance is {self.min_balance} and your current balance is {self.balance}")
        else:
            super().take_out_money(amount)  


def menu():
    print("Welcome to your bank.")
    try:
        initial_balance = float(input("Enter the initial amount of money: "))
        min_balance = float(input("Enter the minimum allowed balance: "))
    except ValueError:
        print("Invalid input. Please enter a numeric value")
        return
    
    account = SavingsAccount(initial_balance, min_balance)

    while True:
        print("""

Select an option:

(1) Add money 
(2) Withdraw money
(3) Exit""")

        try:
            option = int(input())
        except ValueError:
            print("Invalid input. Please enter a valid option")
            continue

        if option == 1:
            try:
                amount = float(input("How much do you want to deposit? "))
                account.add_money(amount)
            except ValueError:
                print("Invalid input. Please enter a numeric value")
        elif option == 2:
            try:
                amount = float(input("How much do you want to withdraw? "))
                account.take_out_money(amount)
            except ValueError:
                print("Invalid input. Please enter a numeric value")
        elif option == 3:
            print("Ending session. Goodbye!")
            break
        else:
            print("Invalid option. Please try again")

menu()
