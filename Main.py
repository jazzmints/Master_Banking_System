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

    removeCustomer = DeleteCustomer()


    bank.add_customer(Customer("Jaz",12345,54321))
    bank.add_customer(Customer("Zay",6789,9876))
    bank.add_customer(Customer("Sam",12345,54321))


    while True:
        menu.show_menu()
        choice=int(input("Enter menu choice:"))

        if choice == 1:

            createCustomer.create_customer(bank)
            

        elif choice == 2:
            readCustomer.display_bank(bank)


        elif choice == 4:
            removeCustomer.remove_customer(bank)

        elif choice == 5:
            print("\n Thank you for using the bank system!")
            break

        else:
            print("Invalid Menu Option")

if __name__ == "__main__":
    main()