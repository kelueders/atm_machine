'''
Description: This application asks a user to enter their account holder name,
    account number, and account balance and saves it to a file. It then displays
    a menu asking if the user wants to deposit, withdraw, check balance, add 
    a new customer's information, or change customers for withdrawal/deposit actions.

Course Name: Programming Logic & Technique

Course Num: CIS1400-NET02

Assignment: Assignment #3

Author: Kate Lueders

Version: 1.0

Date: 08/03/2025

Input: string, string, float, float

Output: int, prints to console
'''

def main():
    # Declare variables
    menu_option = 0
    name = ""

    if not name:
        name = collect_info()

    # Lead user through the menu options
    while menu_option != 6:

        # Read the customer file and set the variables to the contents of the file
        customer_info = read_file(name)
        name = customer_info[0]
        account_num = customer_info[1]
        account_bal = customer_info[2]

        print("")
        print("Please select from the following ATM options: ")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Enter new customer info")
        print("5. Change customers")
        print("6. Exit")
        try:
            menu_option = int(input("Enter number here: "))
        except ValueError:
            print("")
            print("**Invalid entry. Please enter only 1, 2, 3, 4, 5, 6")
            continue
        print("")

        match menu_option:
            case 1:
                account_bal = deposit(account_bal)
                write_file(name, account_num, account_bal)
            case 2:
                account_bal = withdrawal(account_bal)
                write_file(name, account_num, account_bal)
            case 3:
                check_balance(name, account_num, account_bal)
            case 4:
                collect_info()
            case 5:
                name = input("Account holder name: ")
            case 6:
                # EXIT
                check_balance(name, account_num, account_bal)
                print("Thank you. Have a great day!")
            case _:
                print("**Invalid entry. Please enter only 1, 2, 3, or 4")

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
    return name

def write_file(name, account_num, account_balance):
    data = open(f'P4ATMdata.txt', 'w')

    data.write(f'{name}, {account_num}, {account_balance:.2f}\n')

    data.close()

def read_data(file):
    data = open(f'{file}', 'r')
    name_arr = []
    account_num_arr = []
    account_bal_arr = []

    for d in data:
        customer_record = d.strip().split(", ")
        name_arr.append(customer_record[0])
        account_num_arr.append(customer_record[1])
        account_bal_arr.append(float(customer_record[2]))

    data.close()

    return [name_arr, account_num_arr, account_bal_arr]

if __name__ == "__main__":
    main()




