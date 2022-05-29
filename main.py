import Entities
import csv

# ------------------------------- Customer Input List ----------------------------------

customerInputList = []  #create a list variable for the customer_input file

# read the csv file without using pandas and parse it into the CustomerInput entity
with open('CUSTOMER_INPUT.csv', 'r') as file:
    my_reader = csv.reader(file, delimiter=',')
    for row in my_reader:
       customerInputList.append(Entities.CustomerInput(row))

customerInputList.pop(0)   # Remove the header from the entity object

# Do the same for the other csv files

# ------------------------------- Customer List ------------------------------------------

CustomerList = [] # Create a list variable to parse in the customers csv file

# Read the csv file without using pandas and parse it into the Customer entity
with open('CUSTOMER.csv', 'r') as file:
    my_reader = csv.reader(file, delimiter=',')
    for row in my_reader:
       CustomerList.append(Entities.Customer(row[0],row[1],row[2]))

CustomerList.pop(0)   # Remove the header from the entity object

# ----------------------------------- Invoice List -------------------------------------

InvoiceList = []  # Create a list variable to parse in the invoice csv file

# Read the csv file without using pandas and parse it into the Invoice entity
with open('INVOICE.csv', 'r') as file:
    my_reader = csv.reader(file, delimiter=',')
    for row in my_reader:
       InvoiceList.append(Entities.Invoice(row[0],row[1],row[2],row[3]))

InvoiceList.pop(0)    # Remove the header from the entity object

# ------------------------------------- Invoice Item List ----------------------------------------

InvoiceItemList = []  # Create a list variable to parse in the invoice_item csv file

# Read the csv file without using pandas and parse it into the InvoiceItem entity
with open('INVOICE_ITEM.csv', 'r') as file:
    my_reader = csv.reader(file, delimiter=',')
    for row in my_reader:
       InvoiceItemList.append(Entities.InvoiceItem(row[0],row[1],row[2],row[3]))

InvoiceItemList.pop(0)    # Remove the header from the entity object

#  ----------------------------------------  Main code  --------------------------------------

# Create an empty list that will hold all the customers from CUSTOMER_INPUT.CSV whose customer code
# exists in CUSTOMER.CSV (which might be our DB) and print them

customerThatExistInTheList = []

for customers in CustomerList:
    for customerInput in customerInputList:
        if(customers.customercode == customerInput.customercode):
            customerThatExistInTheList.append(customers)
            print(customerThatExistInTheList)





#  Create an empty list that will hold all the invoices from INVOICE.CSV whose customer code
#  exists in customerThatExistInTheList

invoicesThatExistInTheList = []
for invoice in InvoiceList:
    for customersThatExist in customerThatExistInTheList:
        if(invoice.customercode == customersThatExist.customercode):
            invoicesThatExistInTheList.append(invoice)
            print(invoicesThatExistInTheList)



#  Create an empty list that will hold all the invoice items from INVOICE_ITEM.CSV whose invoice code
#  exists in invoicesThatExistInTheList

invoiceItemsThatExistInTheList = []
for invoiceItem in InvoiceItemList:
    for invoiceItemsThatExist in invoicesThatExistInTheList:
        if(invoiceItem.invoicecode == invoiceItemsThatExist.invoicecode):
            invoiceItemsThatExistInTheList.append(invoiceItem)
            print(invoiceItemsThatExistInTheList)