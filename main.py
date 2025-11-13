def welcome_user():
    print("Hello! Welcome to the Bank Account Assistant Chatbot!")
    print("I can help you explore our account options and get started with signing up.")

def get_user_info():
    name = input("Please enter your name: ")
    while not name:
        name = input("Name cannot be empty. Please enter your name: ").strip()

    age = None
    while age is None:
        try:
            age_input = input("Please enter your age: ")
            age = int(age_input)
            if age <= 0:
                print("Please enter a valid age greater than 0.")
                age = None
        except ValueError:
            print("Please enter a valid number for age.")
    return name, age

def display_main_menu():
    print("How can I help you today? Please choose an option:")
    print("1. Explore Account Options (Checking vs. Savings)")
    print("2. Start the Sign-Up Process")
    print("3. Check Today's Interest Rates")
    print("4. Exit")

def explore_accounts_menu():
    print("--- Explore Account Options ---")
    print("Which type of account are you interested in learning about?")
    print("1. Checking Account")
    print("2. Savings Account")
    print("3. Back to Main Menu")

    choice = input("Enter the number of your choice (1-3): ")

    if choice == "1":
        print("--- Checking Account Details ---")
        print("- Designed for everyday transactions (bills, purchases).")
        print("- Easy access to your money via debit card and checks.")
        print("- May have monthly fees or minimum balance requirements.")
        print("- Learn more on our website or choose option 2 from the main menu to start signing up!")
    elif choice == "2":
        print("--- Savings Account Details ---")
        print("- Designed for saving money and earning interest.")
        print("- Access is less frequent than checking (withdrawals may be limited).")
        print("- Helps build financial security over time.")
        print("- Learn more on our website or choose option 2 from the main menu to start signing up!")
    elif choice == "3":
        return # Go back to the main loop
    else:
        print("Invalid choice. Returning to the main menu.")

def start_signup_process(name, age):
    print(f"Great, {name}! Let's begin the sign-up process.")
    
    account_choice = ""
    while account_choice not in ("1", "2"):
        print("Which account would you like to open?")
        print("1. Checking Account")
        print("2. Savings Account")
        account_choice = input("Enter your choice (1 or 2): ")
        if account_choice == "1":
            account_type = "Checking"
        elif account_choice == "2":
            account_type = "Savings"
        else:
            print("Invalid choice. Please try again.")

    print(f"Okay, a {account_type} Account it is.")
    
    ssn = ""
    while not ssn.isdigit() or len(ssn) != 9:
        ssn = input("Please enter your 9-digit Social Security Number (for validation purposes): ")
        if not ssn.isdigit() or len(ssn) != 9:
            print("Invalid input. Please enter a 9-digit number.")
            
    print("--- Terms and Conditions ---")
    print("Please read the following terms:")
    print("1. By proceeding, you agree to a credit check.")
    print("2. You agree to our privacy policy regarding the handling of your data.")
    print("3. This account will be subject to standard fees and rates.")
    
    agreed = ""
    while agreed.lower() not in ("yes", "y"):
        agreed = input("Do you agree to the terms and conditions? (yes/no): ")
        if agreed.lower() == "no" or agreed.lower() == "n":
            print("You must agree to the terms to continue with the sign-up process.")
            return 
        elif agreed.lower() not in ("yes", "y"):
            print("Please answer with 'yes' or 'no'.")

    print("--- Confirmation ---")
    print(f"Thank you, {name}! You have successfully completed the sign-up process for a {account_type} Account.")
    print("A confirmation email will be sent to your registered email address with further instructions.")
    print("Welcome to our bank!")

def check_interest_rates():
    print("--- Current Interest Rates (APY) ---") 
    print(f"As of today:")
    print(" - Standard Savings Account: 0.40% APY")
    print(" - High-Yield Savings Account: 4.25% APY")
    print(" - Checking Account (Interest Bearing): 0.10% APY")
    print("Rates are subject to change. Check our website for the most up-to-date information.")

#main menu
def main():
    welcome_user()
    name, age = get_user_info()
    print(f"Nice to meet you, {name}! Let's find the right account for you.")

    while True:
        display_main_menu()
        choice = input("Enter the number of your choice (1-4): ")

        if choice == "1":
            explore_accounts_menu()
        elif choice == "2":
            start_signup_process(name, age)
        elif choice == "3":
            check_interest_rates()
        elif choice == "4":
            print(f"Goodbye, {name}! Thanks for chatting with our banking assistant.")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 4.")

if __name__ == "__main__":
    main()