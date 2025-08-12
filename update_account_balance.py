def update_account_balance(name, account_num, account_balance):
    # Read all lines from the file
    try:
        with open('P4ATMdata.txt', 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        lines = []

    updated = False
    new_lines = []
    for line in lines:
        customer_record = line.strip().split(", ")
        if len(customer_record) >= 2 and customer_record[1] == account_num:
            # Update this line with new balance
            new_lines.append(f"{name}, {account_num}, {account_balance:.2f}\n")
            updated = True
        else:
            new_lines.append(line)
    if not updated:
        # If account not found, add new record
        new_lines.append(f"{name}, {account_num}, {account_balance:.2f}\n")

    with open('P4ATMdata.txt', 'w') as file:
        file.writelines(new_lines)
