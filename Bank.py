# Bank
from Customer import Customer

# Defining Bank
class Bank:
    customers = Customer()
    def __init__(self):

        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)

    def get_customer(self):
        return self.customers()

    def remove_customer(self, customer):
        self.customers.remove(customer)

    def get_customer(self, customer):
        self.customers.index(customer)