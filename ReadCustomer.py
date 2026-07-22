from CreateCustomer import CreateCustomer

class ReadCustomer:

    def __init__(self):
        self.customers = []

    def display_bank(self):
        print("Customers")
        print("---------")

        for customer in self.customers:
            customer.show_customer()
            print()