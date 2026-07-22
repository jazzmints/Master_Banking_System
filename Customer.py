class Customer:

    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def show_customer(self):
        print("Enter Name: ", self.name)
        print("Account_Number: ", self.account_number)
        print("Balance: ", self.balance)

