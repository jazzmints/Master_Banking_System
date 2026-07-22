from Bank import Bank
from Customer import Customer
from ReadCustomer import ReadCustomer

class DeleteCustomer:

    def __init__(self, account_number, customer):
        self.account_number = account_number
        self.customer = customer

    def delete(self, account_number, customer):
        account_number = int(input("Enter account number to delete: "))

        customer = bank.find_customer(account_number)

        if customer:
            customer.remove_customer()
            