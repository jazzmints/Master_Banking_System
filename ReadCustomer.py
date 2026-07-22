from CreateCustomer import CreateCustomer
from Bank import Bank
from Customer import Customer

class ReadCustomer:

    def __init__(self, bank):
        self.bank = bank
        
    def display_bank(self, bank):
        print("Customers")
        print("---------")

        bank.get_customer()

        if not self.customers():
            print("No Customers Found!")
            return

        for customer in self.customers():
            customer.show_customer()