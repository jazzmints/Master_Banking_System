from CreateCustomer import CreateCustomer
from Bank import Bank
from Customer import Customer

class ReadCustomer:


    def display_bank(self, bank):
        print("Customers")
        print("---------")

        customers = bank.get_customer()

        if not customers:
            print("No Customers Found!")
            return

        for customer in customers:
            customer.show_customer()