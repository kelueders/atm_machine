'''
Description: This application asks a user to enter their account holder name,
    account number, and account balance and saves it to a file. It then displays
    a menu asking if the user wants to deposit, withdraw, check balance, add 
    a new customer's information, or change customers for withdrawal/deposit actions.

Course Name: Programming Logic & Technique

Course Num: CIS1400-NET02

Assignment: Assignment #4

Author: Kate Lueders

Version: 1.0

Date: 08/09/2025

Input: string, string, float, float

Output: int, prints to console
'''

def main():
    # Declare variables
    menu_option = 0
    account_num = None

    while True:
        existing_customer = input("Are you an existing customer? (y/n)")
        if existing_customer == "y":
            menu_option = 5
            break
        elif existing_customer == "n":
            menu_option = 4
            break
        else:
            print("Invalid entry. Please try again.")

    account_num = menu_caller(menu_option)

    while menu_option != 6:
        # Lead user through the menu options
        menu_option = display_menu_and_validate()
        account_num = menu_caller(menu_option, account_num)

def menu_caller(menu_option, account_num=None):


    # Only get customer info for options that require it
    if menu_option in [1, 2, 3, 6]:
        if not account_num:
            print("Error: No account selected. Please select or create an account first.")
            return account_num
        customer_info = read_file(account_num)
        if customer_info is None:
            print("Error: Account not found. Please enter a valid account number.")
            return account_num
        name = customer_info[0]
        account_num = customer_info[1]
        account_bal = customer_info[2]

    match menu_option:
        case 1:
            # Deposit
            account_bal = deposit(account_bal)
            write_file(name, account_num, account_bal)
        case 2:
            # Withdraw
            account_bal = withdrawal(account_bal)
            write_file(name, account_num, account_bal)
        case 3:
            # Check balance
            check_balance(name, account_num, account_bal)
        case 4:
            # Enter new customer information
            account_num = collect_info()
            return account_num
        case 5:
            # Access existing customer account
            account_num = input("Customer account number: ")
            return account_num
        case 6:
            # EXIT
            check_balance(name, account_num, account_bal)
            print("Thank you. Have a great day!")
        case _:
            # Error message
            print("**Invalid entry. Please enter only 1, 2, 3, 4, 5, or 6")

def display_menu_and_validate(menu_option=0):
    print("")
    print("Please select from the following ATM options: ")
    print("[1] Deposit")
    print("[2] Withdraw")
    print("[3] Check balance")
    print("[4] Enter new customer info")
    print("[5] Change customers")
    print("[6] Exit")
    try:
        menu_option = int(input("Enter number here: "))
    except ValueError:
        print("")
        print("**Invalid entry. Please enter only 1, 2, 3, 4, 5, or 6")
    print("")

    return menu_option

def withdrawal(account_balance):
    TRANSACTION_FEE = 1.50
    withdrawal_amt = 0.0

    withdrawal_amt = float(input("How much do you want to withdraw? $"))
    print("")

    # Perform calculations
    withdrawal_plus_fee = withdrawal_amt + TRANSACTION_FEE

    # Determine if there are enough funds in account
    if withdrawal_plus_fee <= account_balance:
        account_balance -= withdrawal_plus_fee
        print(f"**Your new account balance is: ${account_balance:.2f}**")
    else:
        print("Not enough funds in account. Transaction failed.")

    return account_balance

def deposit(account_balance):
    deposit_amt = float(input("How much do you want to deposit? $"))
    print("")

    # Calculate new account balance
    account_balance += deposit_amt
    print(f"**Your new account balance is: ${account_balance:.2f}**")

    return account_balance

def check_balance(name, account_num, account_balance):
    print("**ACCOUNT BALANCE**")
    print(f"Name: {name}")
    print(f"Account Number: {account_num}")
    print(f"Account Balance: ${account_balance:.2f}")

def collect_info():
    # Collect user input
    print("Please enter your information below:")
    print("")
    name = input("Account Holder's Name: ")
    account_num = input("Account Number: ")
    account_bal = float(input("Account Balance: $"))
    print("")
    write_file(name, account_num, account_bal)
    return account_num

def write_file(name, account_num, account_balance):
    records = open(f'records.dat', 'a')

    records.write(f'{name}, {account_num}, {account_balance:.2f}\n')

    records.close()

def read_file(account_num):
    records = open(f'records.dat', 'r')

    for record in records:
        customer_data = record.strip().split(", ")
        if customer_data[1] == account_num:
            name = customer_data[0]
            account_num = customer_data[1]
            account_balance = float(customer_data[2])
            return [name, account_num, account_balance]
        else:
            continue
    print("No account found")

    records.close()

if __name__ == "__main__":
    main()




