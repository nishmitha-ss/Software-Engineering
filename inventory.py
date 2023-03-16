import pandas as pd

pd.options.display.width = None

menu_options = {
    1: 'Add New Product',
    2: 'Add To an existing Product',
    3: 'View Inventory ',
    4: 'View quantity less than 5',
    5: 'Enter warehouse capacity',
    6: 'Exit'
}
def print_menu():
    for key in menu_options.keys():
        print (key, ' ', menu_options[key] )

class Inventory:
    def __init__(self):
        self.inventory = r'inventory.csv'

    def add_newproduct(self, ware_num):
        #Adding new product to the inventory
        view = pd.read_csv(self.inventory)
        if not view.empty:
            #Generating product id
            product_Id = max(view['ProductId']) + 1
        else:
            product_Id = 1
        print("Product Id:",product_Id)
        #Entering required values
        get_capacity = list(view.iloc[:, 0])
        try:
            value = get_capacity.index(ware_num)
            capacity = view.loc[value, 'Warehouse Capacity']
            item = int(input('Select \n 1. TV \n 2. STEREO \n Enter your choice:'))
            if item == 1:
                item_type = 'TV'
            elif item == 2:
                item_type = 'STEREO'
            model_name = input("Enter the Model Name:")
            model_name = model_name.upper()
            cost_price = float(input("Enter Cost Price of Product: $"))
            selling_price = float(input("Enter Selling Price of Product: $"))
            quantity = int(input("Quantity of the Product:"))
            # Insert data into csv file
            data = [[ware_num, capacity, item_type, product_Id, model_name, cost_price, selling_price, quantity]]
            df = pd.DataFrame(data)
            df.to_csv(self.inventory, mode='a', index=False, header=False)
        except:
            print("Invalid Data Entered")


    def add_existingproduct(self,ware_num,model_Id):
        # Adding to inventory a product that already exists(Adds the quantity to existing quantity)
        view = pd.read_csv(self.inventory)
        try:
            item_warehouse = view.loc[view['Warehouse'] == ware_num]
            product = list(item_warehouse.iloc[:, 3])
        except:
            print("Enter valid Warehouse number or Model_Id")

        try:
            value = product.index(model_Id)
            quantity = int(input("Enter Quantity of product:"))
            insert_quantity = item_warehouse.loc[value, 'Quantity']
            insert_quantity = insert_quantity + quantity
            product = list(view.iloc[:, 3])
            value = product.index(model_Id)
            view.loc[value, 'Quantity'] = insert_quantity
            view.to_csv(self.inventory, index=False)
        except:
            print("Invalid Data Entered")


    def view_inventory(self,ware_num):
        # View The products in a particular warehouse
        view = pd.read_csv(self.inventory, usecols=["Warehouse", "Item Type", "Model", "Quantity"] )
        value = list(view.iloc[:, 0])
        try:
            if ware_num in value:
                item_warehouse= view.loc[view['Warehouse'] == ware_num]
                if not item_warehouse.empty:
                    print(item_warehouse)
                else:
                    print("NO Data present")
            else:
                print("Enter Valid Warehouse number")
        except:
            print("Enter Valid Warehouse number")

    def view_lessthan5(self,ware_num):
        # View products less than 5 in a particular warehouse
        view = pd.read_csv(self.inventory)
        value = list(view.iloc[:,0])
        try:
            if ware_num in value:
                item_warehouse = view.loc[view['Warehouse'] == ware_num]
                getlist = item_warehouse.loc[view['Quantity'] < 5]
                getlist = getlist.sort_values(['Quantity'], ascending=[True])
                if not getlist.empty:
                    print(getlist)
                else:
                    print("No data present")
            else:
                print("Enter Valid Warehouse")
        except:
            print("Invalid Data")

    def enter_warehousecapacity(self,ware_num):
        #Entering the capacity of the warehouse
         view = pd.read_csv(self.inventory)
         value = list(view.iloc[:, 0])
         try:
             if ware_num in value:
                capacity = int(input('Enter Warehouse Capacity:'))
                view.loc[view['Warehouse'] == ware_num, 'Warehouse Capacity'] = capacity
                view.to_csv(self.inventory, index=False)
             else:
                print("Enter Valid Warehouse number")
         except:
            print("Invalid data Entered")

if __name__ == '__main__':
    while (True):
        print_menu()
        ElectronicInventory= Inventory()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')

        if option == 1:
            try:
                ware_num = int(input('Select Warehouse (1 or 2): '))
                ElectronicInventory.add_newproduct(ware_num)
            except:
                print("Enter valid warehouse number")

        elif option == 2:
            try:
                ware_num = int(input('Select Warehouse (1 or 2): '))
                model_Id = int(input("Enter Model Id to add products:"))
                ElectronicInventory.add_existingproduct(ware_num, model_Id)
            except:
                print("Enter valid warehouse number or model Id")

        elif option == 3:
            try:
                ware_num = int(input('Select Warehouse (1 or 2): '))
                ElectronicInventory.view_inventory(ware_num)
            except:
                print("Enter valid warehouse number")

        elif option == 4:
            try:
                ware_num = int(input('Select Warehouse (1 or 2):'))
                ElectronicInventory.view_lessthan5(ware_num)
            except:
                print("Enter valid Warehouse Number")

        elif option == 5:
            try:
                ware_num = int(input('Select Warehouse (1 or 2): '))
                ElectronicInventory.enter_warehousecapacity(ware_num)
            except:
                print("Enter Valid Warehouse Number")

        elif option == 6:
            print('Thank you')
            exit()

        else:
            print('Invalid option. Please enter a number between 1 and 6')