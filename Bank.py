# Bank
from Customer import Customer

# Defining Bank
class Bank:
    customers = Customer()
    def __init__(self):
        self.customers = []

    def add_customer(self):
        for customer in self.customers:
            self.customers.append(customer)

    def find_customer(self):
        for customer in self.customers:
            if customer in self.customers:
                print(customer)

    def remove_customer(self):
        for customer in self.customers:
            if customer in self.customers:
                self.customers.remove(customer)

    def get_customer(self):
        for customer in self.customers:
            if customer in self.customers:
                self.customers.index(customer)