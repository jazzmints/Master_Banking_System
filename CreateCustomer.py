from Bank import Bank
from Customer import Customer

class CreateCustomer:

    def create_customer(self, bank):
        name = input("Enter customer name:")
        account_number = int(input("Enter account number:"))
        balance = float(input("Enter starting balance:"))

        customer = Customer(name, account_number, balance)
        bank.add_customer(customer)

        print("Customer created successfully!")
