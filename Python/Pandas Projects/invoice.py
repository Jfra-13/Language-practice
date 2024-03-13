''' GESTOR DE FACTURAS '''

import random

def invoice_key ():
    return random.randint(100, 999)

def insert_invoice ():
    final_add = int(input('Write amount of invoice: '))
    for _ in range(final_add):
        k = invoice_key()
        v = float(input('Write the price of the invoice: '))
        invoice_storage[k] = v
    print('------Uploaded invoices------')

def payment_invoice():
    print('------Invoices to pay------')
    for key, value in invoice_storage.items():
        print(f'Invoice {key}: ${value}')

    final_pay = int(input('Enter the number of invoices to be paid:  '))
    for _ in range(final_pay):
        select_invoice = int(input('Choose the invoice code you want to pay: '))
        if select_invoice in invoice_storage:
            del invoice_storage[select_invoice]
        else:
            print('Invoice not found. Please enter a valid invoice code.')
    print('------Paid documents------')   
    
     
print('Open system')
invoice_storage = {}

while True:
  
    action = str(input('Do you want to Add an Invoice (A), Pay an Invoice (P), or End the Process (E)? ').upper())
    if action == 'A':
        insert_invoice()
    elif action == 'P':
        payment_invoice()
    elif action == 'E':
        print('Process completed')
        break
    else:
        print('Invalid input. Please enter A to add, P to pay, or E to end the process.')
    

    


    


