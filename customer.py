import pandas as pd
from pandas import DataFrame
pd.options.display.width = None

menu_options = {
    1: 'Register Customer Details',
    2: 'View Customer Detail',
    3: 'Edit customer Details',
    4: 'Exit'
}

def print_menu():
    for key in menu_options.keys():
        print(key, ' ', menu_options[key])

class Customer:
    def __init__(self):
        self.customer = r'customer.csv'

    def register_customer(self,name):
        read = pd.read_csv(self.customer)
        # Input : Customer Name
        # Checking if customer name  entered is numeric. If yes its invalid
        if name.isnumeric() == True:
            print("Enter Valid Name")
        else:
            try:
                # Checking if Customer naem is already present in the csv file.If not present insert into csv file
                if name not in read.values:
                    # Generating customer ID
                    if not read.empty:
                        id = max(read['Customer Id']) + 1
                    else:
                        id = 1
                    print("Customer Id:", id)
                    taxper = int(input("Enter Tax Percentage:"))
                    data1 = [[id, name, taxper]]
                    df2 = DataFrame(data1)
                    #Insert customer info into customer.csv
                    df2.to_csv(self.customer, mode='a', index=False, header=False)
                else:
                    print("Customer Already registered")
            except:
                print("Invalid Data Entered")

    def view_customerdetails(self,id):
        read = pd.read_csv(self.customer)
        # Input = Customer ID
        # Storing customer Id in a list to get index of the customer detail in Csv file and display information.
        custid = list(read.iloc[:, 0])
        try:
            if id in custid:
                value = custid.index(id)
                view = read.loc[read['Customer Id'] == id]
                print(view)
            else:
                print("Invalid Data Entered")
        except:
            print("Invalid Data")

    def edit_customerdetails(self,id):
        read = pd.read_csv(self.customer)
        # Input =Customer Id
        # Storing customer Id in a list to get index of the customer detail in Csv file and update the Tax of the customer
        custid = list(read.iloc[:, 0])
        try:
            if id in custid:
                value = custid.index(id)
                taxper = int(input("Enter Tax Percentage:"))
                read.loc[value, 'Tax Percentage'] = taxper
                read.to_csv(self.customer, index=False)
            else:
                print("Invalid Data Entered")
        except:
                print("Enter Valid values")

if __name__ == '__main__':
    while (True):
        print_menu()
        ElectronicCustomer= Customer()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')

        if option == 1:
            try:
                name = (input('Customer Name:'))
                name = name.upper()
                ElectronicCustomer.register_customer(name)
            except:
                print("Enter Valid Values")
        if option == 2:
            try:
                id= int(input("Enter Customer Id:"))
                ElectronicCustomer.view_customerdetails(id)
            except:
                print("Enter Valid Values")
        if option == 3:
            try:
                id= int(input("Enter Customer Id:"))
                ElectronicCustomer.edit_customerdetails(id)
            except:
                print("Enter Valid Values")
        elif option == 4:
            print('Thank you')
            exit()











