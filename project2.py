bank_data = {}

def new_customer():
    print("\n Create New Account")
    acc_no = int(input("Enter account number: "))
    
    if acc_no in bank_data:
        print(" Account already exists!")
        return
    
    name = input("Enter Name: ")
    address = input("Enter Address: ")
    phone = input("Enter Phone: ")
    acc_type = input("Enter Account Type (Saving/Current): ")
    amount = float(input("Enter Initial Amount: "))

    bank_data[acc_no] = {"Name": name,"Address": address,"Phone": phone,"Account_Type": acc_type,"Balance": amount}
        
    print("\n Account Created Successfully!")


def existing_customer():
    print("\nExisting Customer")
    acc_no = int(input("Enter account number: "))
    
    if acc_no not in bank_data:
        print("Account not found!")
        return
    
    print("\nCustomer Details:")
    for key, value in bank_data[acc_no].items():
        print(f"{key}: {value}")
    
    print("\n1. Deposit Money\n2. Withdraw Money\n3. Check Balance\n4. Back to Main Menu")
    choice = int(input("Enter choice: "))
    
    if choice == 1:
        amount = float(input("Enter deposit amount: "))
        bank_data[acc_no]["Balance"] += amount
        print(f" Deposit successful! New Balance: {bank_data[acc_no]['Balance']}")
    
    elif choice == 2:
        amount = float(input("Enter withdrawal amount: "))
        if amount > bank_data[acc_no]["Balance"]:
            print("️ Insufficient Balance!")
        else:
            bank_data[acc_no]["Balance"] -= amount
            print(f" Withdrawal successful! New Balance: {bank_data[acc_no]['Balance']}")
    
    elif choice == 3:
        print(f" Current Balance: {bank_data[acc_no]['Balance']}")
    
    else:
        print("Returning to main menu...")


def main():
    while True:
        print("\n----------------------------")
        print("      Bank Management System")
        print("----------------------------")
        print("1. New Customer")
        print("2. Existing Customer")
        print("3. Exit")
        
        choice = int(input("Enter choice: "))
        
        if choice == 1:
            new_customer()
        elif choice == 2:
            existing_customer()
        elif choice == 3:
            print(" Thank you for using our system!")
            break
        else:
            print(" Invalid choice! Please try again.")



main()
