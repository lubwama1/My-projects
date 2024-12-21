

from getpass import getpass
import time
from datetime import datetime
import os

# Initialize variables
account_balance = 4000
pin = 88507
pin_attempts = 3

# Function to get the current date and time
def date_transaction():
    return datetime.now()

# Function to define the main menu options
def menu():
    return {
        1: 'Send Money',
        2: 'Airtime & Bundles',
        3: 'Withdrawal',
        4: 'Check Balance'
    }

# Function for sending money
def send_money():
    return {
        1: 'Airtel Number',
        2: 'MTN Number'
    }, ['075', '070'], ['077', '071']

# Function for airtime and bundles
def airtime_bundles():
    return {
        'Airtime': {1: 'Yourself', 2: 'Another Number'},
        'Bundles': {1: 'Yourself', 2: 'Another Number'}
    }, ['075', '070'], ['077', '071'], {500: '25MB', 1000: '50MB', 2000: '100MB'}

# Display the menu
def display_menu():
    global account_balance
    while True:
        os.system('clear')
        print('Select Option:')
        print('~~' * 15)
        menu_options = menu()
        for key, value in menu_options.items():
            print(f'{key}: {value}')
        try:
            choice = int(input('\nEnter your choice: '))
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
                input('\nPress Enter to return to the menu.')
            else:
                print('Invalid option selected.')
        except ValueError:
            print('Please enter a valid number.')
        except Exception as e:
            print(f'Error: {e}')

# Function for sending money
def send_money_choice():
    global account_balance, pin_attempts
    send_money_option, airtel_code, mtn_code = send_money()
    print('Send Money Option:')
    for key, value in send_money_option.items():
        print(f'{key}: {value}')
    try:
        choice = int(input('\nEnter your choice: '))
        if choice not in send_money_option:
            print('Invalid option selected.')
            return
        number = input('Enter number: ')
        valid_codes = airtel_code if choice == 1 else mtn_code
        if not (number[:3] in valid_codes and len(number) == 10):
            print('Invalid number format. Please ensure the number has 10 digits and a valid prefix.')
            return
        amount = int(input('Enter amount: '))
        if amount > account_balance:
            print('Insufficient balance.')
        elif amount <= 0:
            print('Amount must be greater than zero.')
        else:
            pincode = getpass('Enter Pin: ')
            if pincode == str(pin):
                account_balance -= amount
                print(f'Transaction successful. New balance: UGX {account_balance}')
                print(date_transaction())
            else:
                pin_attempts -= 1
                print(f'Incorrect pin. {pin_attempts} attempts remaining.')
    except ValueError:
        print('Please enter valid numeric inputs.')
    except Exception as e:
        print(f'Error: {e}')

# Function for airtime and bundles
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
                account_balance -= amount
                print(f'{category_name} successfully loaded. New balance: UGX {account_balance}')
                print(date_transaction())
            else:
                pin_attempts -= 1
                print(f'Incorrect pin. {pin_attempts} attempts remaining.')
    except ValueError:
        print('Please enter valid numeric inputs.')
    except Exception as e:
        print(f'Error: {e}')

# Function for withdrawal (placeholder)
def withdrawal_choice():
    print('Withdrawal functionality is not implemented yet.')

# Start the program
if __name__ == '__main__':
    display_menu()