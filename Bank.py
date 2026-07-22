# Bank
from Customer import Customer

# Defining Bank
class Bank:
    
    def __init__(self, customer):
        customer = Customer()
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)

    def find_customer(self, customer):
        self.customers.index(customer)

    def remove_customer(self, customer):
        self.customers.remove(customer)

    def get_customer(self):
        return self.customers()

