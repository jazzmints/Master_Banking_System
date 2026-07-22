from CreateCustomer import CreateCustomer
from Bank import Bank
from Customer import Customer

class ReadCustomer:

    def __init__(self, bank):
        self.bank = bank

    def display_bank(self):
        print("Customers")
        print("---------")

        customers = self.bank.get_customer()

        if not customers:
            print("No Customers Found!")
            return

        for customer in customers:
            customer.show_customer()