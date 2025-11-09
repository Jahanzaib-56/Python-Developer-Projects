class Bank:

    def __init__(self):

        self.balance = 0

    def deposit(self):

        amount = int(input("Enter the amount you want to deposit: "))

        self.balance += amount

        print(f"Your account has been credited with ${amount}")

    def withdraw(self):

        amount = int(input("Enter the amount you want to withdraw: "))
        
        if amount < self.balance:

            self.balance -= amount

            print(f"${amount} has been withdrawed successfully")

        else:
            print("Insufficient balance")

            return self.balance

    def check_money(self):

        print(f"You have ${self.balance} in your account")

def main():

    print("***-----Bank Management System-----***")

    bank = Bank()

    while True:

        print("1. Deposit Money")

        print("2. Withdraw Money")

        print("3. Check Balance")

        print("4. Exit the app")

        choice = int(input("Enter your choice: "))

        if choice == 1:

            bank.deposit()

        elif choice == 2:

            bank.withdraw()

        elif choice == 3:

            bank.check_money()

        elif choice == 4:

            print("Thanks for choosing us")
            
            break

        else:

            print("Invalid Input!!")

if __name__ == "__main__":

    main()