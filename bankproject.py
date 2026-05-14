# --- 1. SETUP AREA (Multi-User Data) ---
# Account Number : {Name, PIN, Balance, History, Loan_status}
import datetime

# --- 1.1 SETUP AREA ---

bank_data = {
    101: {"name": 'Smit', "pin": 1111, "balance": 10000000, "history": [] ,"loan_status": "No Active Loan", "is_locked": False,
        "document": "Aadhar Card (Verified)"},
    102: {"name": 'Darsh', "pin": 2222, "balance": 10000000, "history": [] ,"loan_status": "No Active Loan", "is_locked": False,
        "document": "Aadhar Card (Verified)"},
    103: {"name": 'Devarsh', "pin": 3333, "balance": 10000000, "history": [] ,"loan_status": "No Active Loan", "is_locked": False,
        "document": "Aadhar Card (Verified)"},
    104: {"name": 'Raja', "pin": 4444, "balance": 1000000, "history": [] ,"loan_status": "No Active Loan", "is_locked": False,
        "document": "Aadhar Card (Verified)"},
    105: {"name": 'Om', "pin": 5555, "balance": 1000000000, "history": [] ,"loan_status": "No Active Loan", "is_locked": False,
        "document": "Aadhar Card (Verified)"},
    106: {"name": 'Aryan', "pin": 6666, "balance": 10000000, "history": [] ,"loan_status": "No Active Loan", "is_locked": False,
        "document": "Aadhar Card (Verified)"},
}

def get_time():
    return datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

while True :
    print("\n" + "="*35)
    print("      SABKA BHALAAA DIGITAL BANK     ")
    print("1. Login to Account")
    print("2. Open New Account (Join Us!)")
    print("3. Exit System")
    start_choice = input("Select: ")
    
    if start_choice == '3':
        print("Exiting... Have a nice day!")
        break
    
    # ---2. REGISTRATION ---
    if start_choice == '2':
        new_acc = max(bank_data.keys()) + 1
        name = input("Enter your name: ")
        new_pin = int(input("Set 4-digit PIN: "))
        initiat_amt = float(input("Initial Deposit Amount: "))
        
        bank_data[new_acc] = {
            "name": name, "pin": new_pin, "balance":initiat_amt,
            "history": [f"Account Opened on {get_time()}"],
            "loan_status": "No Active Loan", "is_locked": False,
            "documrnt": "Aadhar Card (Pending Verification)"
        }
        print(f" Success! Your New Account Number is: {new_acc}")
        continue # back in main menu
    
    # ---3. LOGIN AREA (Account No. & PIN Check) ---
    if start_choice =='1':
        acc_no = int(input("Enter Account Number: "))

        if acc_no in bank_data:
            # jo Account already login hoy to...
            if bank_data[acc_no].get("is_locked", False):
                print(" Your account is LOCKED! Please contect the nearest branch.")
                continue # again asked account No.
            
            user_pin = int(input("Enter your 4-Digit PIN: "))

            # Checking if PIN matches for that specific Account Number 
            if user_pin == bank_data[acc_no]["pin"]:
                print(f"\nWelcome, {bank_data[acc_no]['name']}!")
                current_user = bank_data[acc_no] #pointing to the logged-in user

                # --- 4. TRANSACTION MENU AREA (Nested loop for transactions) ---
                while True :
                    print("\n===WELCOME TO SABKA BHALAAA BANK ===")
                    print("\n1. Balance | 2. Deposit | 3. Withdraw | 4. History | 5. Loan | 6. Change PIN | 7. Profile | 8. Transfer | 9.Logout ")
                    choice = input("Select Option: ")

                    if choice == '1':
                        print(f"Current Balance : Rs. {current_user['balance']}")

                    elif choice == '2':
                        amt = float(input("Amount to Deposit: "))
                        current_user['balance'] += amt
                        current_user['history'].append(f"Deposited: {amt}")
                        print("Done!")

                    elif choice == '3':
                        amt = float(input("Amount to Withdraw: "))
                        if amt <= current_user['balance']:
                            current_user['balance'] -= amt
                            current_user['history'].append(f"Withdraw: {amt}")
                            print("Withdrawal Successful!")
                        else:
                            print("Insufficient Funds!")

                    elif choice == '4':
                        print("---History---")
                        if not current_user['history']:
                            print("No transactions yet.")
                        for h in current_user['history']: print(f">{h}")

                    elif choice == '5':
                        #Loan Logic:Give 20% of current balance as loan 
                        #loan_amt = current_user['balance'] * 0.40
                        #print(f"Based on your balance, you are eligible for Rs.{loan_amt} loan.")

                        # 1.Eligibility check (40% of balance)
                        eligible_amt = current_user['balance'] * 0.40

                        if current_user['loan_status'] == "Active Loan":
                            print(" You already have an Active Loan! Please repay it first.")
                        else:
                            print(f" Good News! You are eligible for a loan up to Rs.{eligible_amt}")
                            confirm = input("Do you want to apply for this loan? (yes/no): ").lower().strip()
                            if confirm == 'yes':
                                # 2.Add money to balance
                                current_user['balance'] += eligible_amt

                                # 3. Update Status and History
                                current_user['loan_status'] = "Active Loan"
                                current_user['balance'] += eligible_amt
                                current_user['history'].append(f"Loan Approved: Rs.{eligible_amt}")

                                print(f" Success! Rs.{eligible_amt} has been credited to your account.")
                                print(f"New Balance: Rs.{current_user['balance']}")
                            else:
                                print("Loan application cancelled.")

                    elif choice == '6':
                        
                        attempts = 3  # Attempt counts 

                        while attempts > 0:
                            old_pin = int(input(f"Enter your current PIN ({attempts} attempts left): "))

                            # 1. Old pin check.
                            if old_pin == current_user['pin']:
                                new_pin = int(input("Enter your New 4-Digit PIN: "))
                                confirm_pin = int(input("Confirm your New PIN: "))

                                if new_pin == confirm_pin:
                                    # 2. AUTO-SAVE LOGIC: both side update 
                                    current_user['pin'] = new_pin  # current pin ma save thase
                                    bank_data[acc_no]['pin'] = new_pin  # saved in data base

                                    print("✅ PIN updated successfully and saved!")
                                    break # break the loop
                                else:
                                    print("❌ PIN mismatch! Try the whole process again.")
                                    break
                            else:
                                attempts -= 1
                                if attempts > 0:
                                    print(f"❌ Incorrect PIN. Please try again.")
                                else:
                                    print("⚠️ Too many incorrect attempts. PIN change locked!")
                    elif choice == '7':
                        print("Logging out...")
                        break # Breaks inner Loop, goes back to login Dashboard

                    elif choice == '8':
                        print("\n" + "="*30)
                        print("      USER PROFILE DETAILS      ")
                        print("="*3)
                        # current_user mathi all information le che.
                        print(f"👤 Name           : {current_user['name']}")
                        print(f"🔢 Account No.    : {acc_no}") # login time use kariyu hoy te.
                        print(f"💰 Current Balance: Rs.{current_user['balance']}")
                        print(f"📋 Loan Status    : {current_user.get('loan_status', 'N/A')}")
                        print(f"📄 Documents      : {current_user.get('document', 'None')}")
                        # last history show kare.
                        print("-" * 30)
                        print("Last Transactions:")
                        if current_user['history']:
                            for record in current_user['history'][-3:]: # last 3 entry
                                print(f" -> {record}")
                        else:
                            print(" No transactions yet.")
                            print("="*30)
                            #break

                    elif choice == '9':
                        target_acc = int(input("Enter Recipient's Account Number: "))

                        #check if the targat account exists in our bank_data
                        if target_acc in bank_data and target_acc != acc_no:
                            transfer_amt = float(input(f"Enter amount to transfer to {bank_data[target_acc]['name']}: "))

                            if transfer_amt <= current_user['balance']:
                                # 1. debuct from sender like anyone (smit)
                                current_user['balance'] -= transfer_amt
                                current_user['history'].append(f"sent Rs.{transfer_amt} to Acc {target_acc}")

                                # 2. add to Receiver(Aryan)
                                bank_data[target_acc]['balance'] += transfer_amt
                                bank_data[target_acc]['history'].append(f"received Rs.{transfer_amt} from Acc {acc_no}")

                                print(f"✅ Tarnsaction Successful! Rs.{transfer_amt} sent.")
                            else:
                                print("❌ Insufficient Balance For transfer!")

                        else:
                            print("❌ Invalid Account Number of you cannot transfer to yourself!")   
                            #break

            else:
                print("Invalid PIN!")

        else:
            print("Account Number not Found!") 