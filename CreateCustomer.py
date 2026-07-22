from Bank import Bank
from Customer import Customer

class CreateCustomer:

    def create_customer(self, bank, account_number, name, balance):
        name = input("Enter customer name:")
        account_number = input(int("Enter account number:"))
        balance = float(input("Enter starting balance:"))

        bank.add_customer(name, account_number, balance)

        print("Customer created successfully!")
