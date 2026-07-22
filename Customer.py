class Customer:

    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def show(self):
        print("Enter Name: ", self.name)
        print("Account_Number: ", self.account_number)
        print("Balance: ", self.balance)
        print()

customer1 = Customer()
customer2 = Customer()
customer3 = Customer()

show_customer()
