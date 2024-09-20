def show_message(message):
    print("*********************")
    print(message)
    print("*********************")

def show_balance(balance):
    show_message(f"Your balance is ${balance:.2f}")

def deposit():
    show_message("Enter an amount to be deposited: ")
    try:
        amount = float(input())
        if amount < 0:
            show_message("That's not a valid amount")
            return 0
        else:
            return amount
    except ValueError:
        show_message("Invalid input. Please enter a number.")
        return 0

def withdraw(balance):
    show_message("Enter amount to be withdrawn: ")
    try:
        amount = float(input())
        if amount > balance:
            show_message("Insufficient funds")
            return 0
        elif amount < 0:
            show_message("Amount must be greater than 0")
            return 0
        else:
            return amount
    except ValueError:
        show_message("Invalid input. Please enter a number.")
        return 0

def main():
    balance = 0
    is_running = True

    while is_running:
        show_message("   Banking Program   ")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("*********************")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            show_message("That is not a valid choice")

    show_message("Thank you! Have a nice day!")

if __name__ == '__main__':
    main()
