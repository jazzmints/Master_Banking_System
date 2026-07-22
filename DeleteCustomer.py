from Bank import Bank
from Customer import Customer
from ReadCustomer import ReadCustomer

class DeleteCustomer:


    def remove_customer(self, bank):
        account_number = int(input("Enter account number to delete: "))

        customer = bank.find_customer(account_number)

        if customer:
            bank.remove_customer(customer)
            print("Customer deleted successfully!")

        else:
            print("Customer not found.")
