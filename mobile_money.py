

from getpass import getpass 
import time 
from datetime import datetime 
import os
# Initialize variables
account_balance = 4000
pin = 88507
pin_attempts = 3
delay = time.sleep(1)

# Function to get the current date and time

def date_transaction():
    current = datetime.now()
    formatted_date_time = current.strftime("%Y-%m-%d %I:%M:%p")  # Format: YYYY-MM-DD HH:MM:SS
    return formatted_date_time

# Menu options for the ATM system
def menu():
    menu_options = {
        1: 'Send Money', 
        2: 'Airtime & Bundles',
        3: 'Withdrawal', 
        4: 'Check Balance',
        5: 'Deposit'
    }
    return menu_options

# Function for sending money
def send_money():
    airtel_code = ['075', '070']
    mtn_code = ['077', '071']
    send_options = {
        1: 'Airtel Number', 
        2: 'MTN Number'
    }
    return send_options, airtel_code, mtn_code

# Function for Airtime & Bundles options
def airtime_bundles():
    
    return {
        'Airtime': {1: 'Yourself', 2: 'Another Number'},
        'Bundles': {1: 'Yourself', 2: 'Another Number'}
    }, ['075', '070'], ['077', '071'], {500: '25MB', 1000: '50MB', 2000: '100MB'}

# Function to display the menu
def display_menu():
    menu_options = menu()
    print('Select Option:')
    print('~~' * 15)
    print()
    for key, value in menu_options.items():
        print(f'{key}: {value}')
    
    try:
        print()
        print('~' * 15 )
        choice = int(input('Enter your choice: '))
        if choice == 1:
            os.system('clear')
            send_money_choice()
        elif choice == 2:
            os.system('clear')
            airtime_bundles_choice()
        elif choice == 3:
            os.system('clear')
            withdrawal_choice()
        elif choice == 4:
            os.system('clear')
            print(f'Balance: UGX {account_balance}')
        elif choice == 5:
            os.system('clear')
            deposit_choice()
        else:
            print('Invalid option selected.')
    except Exception as e:
        print(f'Error: {e}')

# Function to handle sending money
# Function to handle sending money
def send_money_choice():
    global account_balance, pin_attempts
    send_money_option, airtel_code, mtn_code = send_money()
    date = date_transaction()
    time.sleep(1)
    print('Send Money Option:')
    print()
    for key, value in send_money_option.items():
        print(f'{key}: {value}')
    
    try:
        print()
        print('~' * 15 )
        choice = int(input('Enter your Choice: '))
        if choice == 1:  # Airtel
            os.system('clear')
            time.sleep(1)
            airtel_number = input('Enter Airtel Number: ')
            #if airtel_number[:3] not in airtel_code:
            if not (airtel_number[:3] in airtel_code and len(airtel_number) == 10):
                print('Invalid Airtel number. Please check the first three digits and ensure the number has 10 digits.')
                return
            print()
            amount = int(input('Enter Amount: '))
            if amount > account_balance:
                print('Insufficient balance. Please reduce the amount.')
            elif amount <= 0:
                print('Amount cannot be zero or negative.')
            else:
                
                pincode = getpass('Enter Pin: ')
                if pincode == str(pin):
                    account_balance -= amount
                    print(f'Transaction successful. New balance: UGX {account_balance}')
                    print(date)
                else:
                    pin_attempts -= 1
                    if pin_attempts == 0:
                        print('Your account is blocked due to too many incorrect pin attempts.')
                    else:
                        print(f'Incorrect pin. {pin_attempts} attempts remaining.')
        elif choice == 2:  # MTN
            os.system('clear')
            time.sleep(1)
            print('Charges may Apply! ')
            print()
            mtn_number = input('Enter MTN number: ')
            
            #if mtn_number[:3] not in mtn_code:
            if not (mtn_number[:3] in mtn_code and len(mtn_number) == 10):
                print('Invalid MTN number. Please check the first three digits and ensure that the number has 10 digits.')
                return
            amount = int(input('Enter Amount: '))
            if amount > account_balance:
                print('Insufficient balance. Please reduce the amount.')
            elif amount <= 0:
                print('Amount cannot be zero or negative.')
            else:
                pincode = getpass('Enter Pin: ')
                if pincode == str(pin):
                    account_balance -= amount
                    print(f'Transaction successful. New balance: UGX {account_balance}')
                    print(date)
                else:
                    pin_attempts -= 1
                    if pin_attempts == 0:
                        print('Your account is blocked due to too many incorrect pin attempts.')
                    else:
                        print(f'Incorrect pin. {pin_attempts} attempts remaining.')
    except Exception as e:
        print(f'Error: {e}')

#Function for airtime and bundles
def airtime_bundles_choice():
    global account_balance, pin_attempts
    airtime_and_data, your_num, another_num, data = airtime_bundles()
    print('Airtime & Data Bundle Options:')
    for idx, category in enumerate(airtime_and_data, 1):
        print(f'{idx}: {category}')
    try:
        category_choice = int(input('\nSelect category (1: Airtime, 2: Bundles): '))
        if category_choice not in [1, 2]:
            print('Invalid category choice.')
            return
        category_name = list(airtime_and_data.keys())[category_choice - 1]
        options = airtime_and_data[category_name]
        print(f'\n{category_name} Options:')
        for key, value in options.items():
            print(f'{key}: {value}')
        selected_option = int(input('\nSelect option (1 or 2): '))
        if selected_option not in options:
            print('Invalid option selected.')
            return
        if selected_option == 1:
            amount = int(input('Enter Amount: '))
        elif selected_option == 2:
            another_number = input('Enter number: ')
            if not (another_number[:3] in another_num and len(another_number) == 10):
                print('Invalid number format. Please ensure the number has 10 digits and a valid prefix.')
                return
            amount = int(input('Enter Amount: '))
        if amount > account_balance:
            print('Insufficient balance.')
        elif amount <= 0:
            print('Amount must be greater than zero.')
        else:
            pincode = getpass('Enter Pin: ')
            if pincode == str(pin):
                if amount in data:
                    account_balance -= amount
                    print(f"{data[amount]} successfully loaded. New balance: UGX {account_balance}")
                    print(date_transaction())
            else:
                pin_attempts -= 1
                print(f'Incorrect pin. {pin_attempts} attempts remaining.')
    except ValueError:
        print('Please enter valid numeric inputs.')
    except Exception as e:
        print(f'Error: {e}')
# Function for withdrawal
def withdrawal_choice():
    global account_balance
    date = date_transaction()
    amount = int(input('Enter Amount: '))
    if amount > account_balance:
        print('Insufficient balance. Please reduce the amount.')
    elif amount <= 0:
        print('Amount cannot be zero or negative.')
    else:
        pincode = getpass('Enter Pin: ')
        if pincode == str(pin):
            account_balance -= amount
            print(f'Withdrawal successful {amount}. New balance: UGX {account_balance}')
            print(date)
        else:
            pin_attempts -= 1
            if pin_attempts == 0:
                print('Your account is blocked due to too many incorrect pin attempts.')
            else:
                print(f'Incorrect pin. {pin_attempts} attempts remaining.')    
    
def deposit_choice():  # Deposit 
    global account_balance
    date = date_transaction()
    airtel_code = ['075', '070']
    mtn_code = ['077', '071']
    try:
        print('Deposit Airtel & MTN')
        print()
        print('1: Airtel')
        print('2: MTN')
        choice = input('Enter option: ')
        
        if choice == '1':  # Airtel Deposit
            airtel_number = input('Enter Airtel Number: ')
            if not (airtel_number[:3] in airtel_code and len(airtel_number) == 10):
                print('Invalid Airtel number format. Ensure it has 10 digits and a valid prefix.')
                return
            amount = int(input('Enter Amount to Deposit: '))
            if amount <= 0:
                print('Amount must be greater than zero.')
                return
            account_balance += amount
            print(f'Deposit successful to {airtel_number}. New balance: UGX {account_balance}')
            print(f'Date: {date}')
        
        elif choice == '2':  # MTN Deposit
            mtn_number = input('Enter MTN Number: ')
            if not (mtn_number[:3] in mtn_code and len(mtn_number) == 10):
                print('Invalid MTN number format. Ensure it has 10 digits and a valid prefix.')
                return
            amount = int(input('Enter Amount to Deposit: '))
            if amount <= 0:
                print('Amount must be greater than zero.')
                return
            else:
                pincode = getpass('Enter Pin: ')
                if pincode == str(pin):
                    account_balance += amount
                    print(f'Deposit successful to {mtn_number}. New balance: UGX {account_balance}')
                    print(f'Date: {date}')
        
                else:
                    pin_attempts -= 1
                    if pin_attempts == 0:
                        print('Your account is blocked due to too many incorrect pin attempts.')
                    else:
                        print(f'Incorrect pin. {pin_attempts} attempts remaining.')    
            
        else:
            print('Invalid option selected.')

    except ValueError:
        print('Please enter a valid numeric value for the amount.')
    except Exception as e:
        print(f'Error: {e}')
# Main code to display the menu
display_menu()