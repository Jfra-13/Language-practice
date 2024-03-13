import random 

def get_NIF ():
   return random.randint(1000, 9999)

def add_customer():
    nif_customer = get_NIF()
    customers[nif_customer] = {'name': '', 'address': '', 'phone': '', 'email': '', 'preferential': None}
    print('---Adding customer---')
    
    for _ in customers[nif_customer]:
        if _ != 'preferential':
            add_data = str(input(f'Write your {_}: '))
            customers[nif_customer][_] = add_data
        else:
            code = '2316'
            add_preference = str(input(f'Enter the preferential customer code: '))
            if add_preference == code:
                customers[nif_customer][_] = True
            else:
                print('Code incorrect')
                customers[nif_customer][_] = False
            
    print(customers)
    
        
    # preferential = input('Write the code if you are preferential: ')

def delete_customer():
    
    print('---Eliminating Customer---')
    print('-Choose a customer to delete ')
    for _ in customers:
        print(f"NIF: {_} | Name: {customers[_]['name']} | Preferential: {customers[_]['preferential']}")
      
    while True:  
        del_by_code = int(input('Enter the customer code to delete: '))        
        if del_by_code in customers :
            customers.pop(del_by_code)
            break
        else:
            print('Incorrect Code')
            

def show_customer():
    print('--Show Customer---')
    choose_cus = str(input('Write to a customer to find: '))
    
    for _ in customers:
        if customers[_]['name'] == choose_cus :
            print(f' NIF: {_} | Name: {customers[_]["name"]} | Preferential: {customers[_]["preferential"]}')

def show_customers():
    print('---Show Customers---')
    for _ in customers:
        print(f' NIF: {_} | Name: {customers[_]["name"]} | Preferential: {customers[_]["preferential"]}')
    
    
def show_prefer_customers():
    print('---Show Customers with Preference---')
    for _ in customers:
        if customers[_]['preferential'] == True:
            print(f' NIF: {_} | Name: {customers[_]["name"]}')


customers = {}
while True:
    action = int(input('Choose the option: \n  -(1) Add Customer\n  -(2) Delete Customer\n  -(3) Show Customer\n  -(4) Show all Customer\n  -(5) Show Prefer Customers\n  -(6) Completed Process -> '))
    
    if action == 1:
        add_customer()
        
    elif action == 2:
        delete_customer()
    elif action == 3:
        show_customer()
    elif action == 4:
        show_customers()
    elif action == 5:
        show_prefer_customers()
    else:
        print('Finished Process')
        break