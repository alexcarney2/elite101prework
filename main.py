
def welcome_user():
    print("Hello! Welcome to the Chatbot!")

def get_user_info():
    name = input("Please enter your name: ")
    while True:
        try:
            age = int(input("Please enter your age: "))
            if age > 0:
                break
            else:
                print("Please enter a valid age greater than 0.")
        except ValueError:
            print("Please enter a valid number for age.")
    return name, age

def display_menu():
    print("\nHow can I help you today? Please choose an option:")
    print("1. Option 1 (Placeholder)")
    print("2. Option 2 (Placeholder)")
    print("3. Option 3 (Placeholder)")
    print("4. Exit")

def main():
    welcome_user()
    name, age = get_user_info()
    print(f"\nNice to meet you, {name}!")

    while True:
        display_menu()
        choice = input("Enter the number of your choice (1-4): ")

        if choice == "1":
            print("You selected Option 1. (Feature not implemented yet)")
        elif choice == "2":
            print("You selected Option 2. (Feature not implemented yet)")
        elif choice == "3":
            print("You selected Option 3. (Feature not implemented yet)")
        elif choice == "4":
            print(f"Goodbye, {name}! Thanks for chatting!")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 4.")

if __name__ == "__main__":
    main()