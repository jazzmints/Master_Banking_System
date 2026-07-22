from Customer import Customer
from Bank import Bank
from CreateCustomer import CreateCustomer
from ReadCustomer import ReadCustomer
from DeleteCustomer import DeleteCustomer
#from UpdateCustomer import UpdateCustomer
from Menu import Menu

def main():

    bank = Bank()
    createCustomer = CreateCustomer()
    readCustomer = ReadCustomer()
    menu = Menu()


    bank.add_customer(Customer("Jaz",12345,54321,500,6895494838))
    bank.add_customer(Customer("Zay",6789,9876,200,676767676767))
    bank.add_customer(Customer("Sam",12345,54321,500,2121212121))


    while True:
        menu.show_menu()
        choice=int(input("Enter menu choice:"))

        if choice == 1:
            account = int(input("Account Number:"))
            name = input("Customer Name:")
            balance = float(input("Opening Balance:"))

            bank.create_customer()
            

        elif choice == 2:
            bank.show_customer()

        elif choice == 3:
            print("\n Thank you for using the bank system!")
            break

        else:
            print("Invalid Menu Option")

if __name__ == "__main__":
    main()