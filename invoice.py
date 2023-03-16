from datetime import datetime
import pandas as pd
from customer import *
pd.options.display.width = None

menu_options = {
    1: 'Create Invoice',
    2: 'Update An invoice Detail',
    3: 'View open invoice',
    4: 'View Closed invoice',
    5: 'Exit'
}

def print_menu():
    for key in menu_options.keys():
        print(key, ' ', menu_options[key])


class Invoice:
    def __init__(self):
        self.customer = r'customer.csv'
        self.invoice = r'create-invoice.csv'
        self.inventory = r'inventory.csv'

    def create_invoice(self, name, model_Id):
        # Input = Customer name , Model Id of product
        today = datetime.today().strftime('%m-%d-%Y')
        lastpayment = datetime.today().strftime('%m-%d-%Y')
        read = pd.read_csv(self.customer)
        # Checking if customer info exists in csv file. If yes exits else ask to Register customer
        if name not in read.values:
            print("Register Customer")
            customer_data = Customer()
            customer_data.register_customer(name)
        else:
            print("Customer registered")
        getid = pd.read_csv(self.invoice)
        # Generate Invoice Id
        if not getid.empty:
            id = max(getid['Id']) + 1
        else:
            id = 1
        print("Invoice Id:", id)
        try:
            address = (input('Customer Address: '))
            address = address.upper()
            phone = int(input('Customer Phone Number: '))
            view = pd.read_csv(self.inventory)
            # Get the product name and selling price using the product Id
            product = list(view.iloc[:, 3])
            value = product.index(model_Id)
            get_quantity = view.loc[value, 'Quantity']
            if get_quantity != 0:
                item = view.loc[value, 'Model']
                print("Item Purchased:", item)
                price = view.loc[value, 'Selling price']
                print("Price of item", price)
                insert_quantity = get_quantity - 1
                view.loc[value, 'Quantity'] = insert_quantity
                view.to_csv(self.inventory, index=False)
            else:
                print("Item not in stock")
            # Getting the Tax percentage Of the customer from customer.csv file
            customer = pd.read_csv(self.customer)
            custname = list(customer.iloc[:, 1])
            value = custname.index(name)
            custax = list(customer.iloc[:, 2])
            taxper = custax[value]
            print('TaxPercent:', taxper, '%')
            tax = (taxper / 100) * price
            tax = round(tax, 2)
            print("Tax: $", tax)
            # Delivery charges
            delivery = float(input('Delivery Charge: $'))
            delivery = round(delivery, 2)
            # Total price of the invoice including Delivery charges and tax
            total = price + tax + delivery
            total = round(total, 2)
            print("Total Amount: $", total)
            discount = str(input('Enter y if customer is paying full at time of purchase else n(y or n):'))
            discount = discount.upper()
            # Discount For the invoice if full amount paid at Time of purchase
            if discount == "Y":
                afterdiscount = total - (total * (10 / 100))
                afterdiscount = round(afterdiscount, 2)
                print("Amount after Discount: $", afterdiscount)
                paid = afterdiscount
                paid = round(paid, 2)
                print("Amount Paid:$", paid)
                topay = 0.00
                topay = round(topay, 2)
                print("Amount To Be Paid:$", topay)
            # No discount
            else:
                afterdiscount = total
                afterdiscount = round(afterdiscount, 2)
                print("Amount after Discount: $", afterdiscount)
                paid = float(input('Amount Paid: $'))
                paid = round(paid, 2)
                topay = afterdiscount - paid
                topay = round(topay, 2)
                if topay > 0:
                    print("Amount To Be paid: $", topay)
                else:
                    print("Enter wrong Amount")
            # Inserting data into invoice.csv file
            data = [
                [today, lastpayment, id, name, address, phone, item, price, taxper, tax, delivery, total,
                 afterdiscount,
                 paid, topay]]
            df = pd.DataFrame(data)
            df.to_csv(self.invoice, mode='a', index=False, header=False)
        except Exception as e:
            print("Enter Valid values")

    def update_invoice(self, id):
        paydate = datetime.today().strftime('%m-%d-%Y')
        update = pd.read_csv(self.invoice)
        # Get invoice from the invoice Id
        invoiceid = list(update.iloc[:, 2])
        try:
            value = invoiceid.index(id)
            name = update.loc[value, 'Customer Name']
            print("Invoice Belongs to:", name)
            newdate = datetime.strptime(paydate, '%m-%d-%Y')
            # Checking if invoice is open or closed.if yes proceeds
            if update.loc[value, 'Amount Left'] != 0:
                purchase_date = update.loc[value, 'Purchase Date']
                purchase_date = datetime.strptime(purchase_date, '%m-%d-%Y')
                getpurchasedate = (newdate - purchase_date).days
                last_date = update.loc[value, 'Last Purchase Date']
                last_date = datetime.strptime(last_date, '%m-%d-%Y')
                getdays = (newdate - last_date)
                getdays = (getdays.days)
                fullamount = (input('Enter if Customer is paying paying full amount(y or n):'))
                fullamount = fullamount.upper()
                # If customer is paying full amount left in the invoice
                if fullamount == 'Y':
                    # within 10 days 10% discount is given.
                    if (getpurchasedate) <= 10:
                        total = update.loc[value, 'Total Amount']
                        afterdiscount = total - (total * (10 / 100))
                        afterdiscount = round(afterdiscount, 2)
                        print("Amount after Discount: $", afterdiscount)
                        print("Amount paid:$", afterdiscount)
                        print("Amount to be paid:$0.00")
                        topay = 0.00
                        update.loc[value, 'After Disc/charge'] = afterdiscount
                        update.to_csv(self.invoice, index=False)
                        update.loc[value, 'Amount Paid'] = afterdiscount
                        update.to_csv(self.invoice, index=False)
                        update.loc[value, 'Amount Left'] = topay
                        update.to_csv(self.invoice, index=False)

                    #If more than 30 days adds 2% tax.
                    elif (getdays) >= 30:
                        topay = update.loc[value, 'Amount Left']
                        charges = (topay * (2 / 100))
                        topay = topay + charges
                        print("2% charge: $", charges)
                        print("Amount to be paid after charges:$", topay)
                        afterdiscount = update.loc[value, 'After Disc/charge']
                        afterdiscount = afterdiscount + charges
                        print("Amount paid:$", topay)
                        print("Amount left: $0.00")
                        topay = 0.00
                        update.loc[value, 'Amount Paid'] = afterdiscount
                        update.to_csv(self.invoice, index=False)
                        update.loc[value, 'Amount Left'] = topay
                        update.to_csv(self.invoice, index=False)
                        update.loc[value, 'After Disc/charge'] = afterdiscount
                        update.to_csv(self.invoice, index=False)

                    else:
                        topay = update.loc[value, 'Amount Left']
                        print("Amount to Be Paid:$", topay)
                        afterdiscount = update.loc[value, 'After Disc/charge']
                        print("Amount paid:$", topay)
                        print("Amount Left to be Paid:$0.00")
                        topay = 0.00
                        update.loc[value, 'Amount Paid'] = afterdiscount
                        update.to_csv(self.invoice, index=False)
                        update.loc[value, 'Amount Left'] = topay
                        update.to_csv(self.invoice, index=False)
                update.loc[value, 'Last Purchase Date'] = paydate
                update.to_csv(self.invoice, index=False)

                # If customer is not paying full amount
                if fullamount == 'N':
                    # After 30 days. Adds 2% charges
                    if (getdays) >= 30:
                        topay = update.loc[value, 'Amount Left']
                        charges = (topay * (2 / 100))
                        charges = round(charges, 2)
                        topay = topay + charges
                        topay = round(topay, 2)
                        print("2% cahrges:$", charges)
                        print("Amount To Be Paid:$", topay)
                        paid = float(input("Amount Paid: $"))
                        topay = topay - paid
                        topay = round(topay, 2)
                        if topay >= 0:
                            print("Amount left to be paid:$", topay)
                            paid = update.loc[value, 'Amount Paid'] + paid
                            afterdiscount = update.loc[value, 'After Disc/charge']
                            afterdiscount = afterdiscount + charges
                            update.loc[value, 'After Disc/charge'] = afterdiscount
                            update.to_csv(self.invoice, index=False)
                            update.loc[value, 'Amount Paid'] = paid
                            update.to_csv(self.invoice, index=False)
                            update.loc[value, 'Amount Left'] = topay
                            update.to_csv(self.invoice, index=False)
                            update.loc[value, 'Last Purchase Date'] = paydate
                            update.to_csv(self.invoice, index=False)
                        else:
                            print("Entered the wrong amount")

                    else:
                        topay = update.loc[value, 'Amount Left']
                        print("Amount to Be Paid:$", topay)
                    paid = float(input("Amount Paid: $"))
                    topay = topay - paid
                    topay = round(topay, 2)
                    if topay >= 0:
                        print("Amount left to be Paid: $", topay)
                        paid = update.loc[value, 'Amount Paid'] + paid
                        update.loc[value, 'Amount Paid'] = paid
                        update.to_csv(self.invoice, index=False)
                        update.loc[value, 'Amount Left'] = topay
                        update.to_csv(self.invoice, index=False)
                        update.loc[value, 'Last Purchase Date'] = paydate
                        update.to_csv(self.invoice, index=False)
                    else:
                        print("Entered wrong Amount")
            else:
                print('Not an Open invoice')
        except:
            print("Enter proper Customer Id")

    def open_invoice(self):
        # Displaying Open invoice
        invoiceopen = pd.read_csv(self.invoice)
        view_open_invoice = invoiceopen.loc[invoiceopen['Amount Left'] > 0]
        view_open_invoice.sort_values('Purchase Date', ascending=True)
        if view_open_invoice.empty:
            print("No open Invoice")
        else:
            print(view_open_invoice)

    def close_invoice(self):
        #Displaying closed invoice
        invoiceclose = pd.read_csv(self.invoice)
        view_close_invoice = invoiceclose.loc[invoiceclose['Amount Left'] == 0]
        view_close_invoice.sort_values('Total Amount', ascending=False)
        if view_close_invoice.empty:
            print("No Closed Invoice")
        else:
            print(view_close_invoice)

if __name__ == '__main__':
    while (True):
        ElectInvoice = Invoice()
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
        if option == 1:

                name = str(input('Customer Name:'))
                name = name.upper()
                model_Id = int(input("Enter Model Id to add products:"))
                ElectInvoice.create_invoice(name, model_Id)

        elif option == 2:
            try:
                id = int(input("Enter Invoice Id:"))
                ElectInvoice.update_invoice(id)
            except:
                print("Wrong input")
        elif option == 3:
            ElectInvoice.open_invoice()
        elif option == 4:
            ElectInvoice.close_invoice()
        elif option == 5:
            print('Thank you')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 5')
