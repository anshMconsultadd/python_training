def atm_simulator():
    balance = 1000.0  

    while True:
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                print(f"Your current balance is: ${balance}")

            elif choice == 2:
                amount = float(input("Enter the amount to deposit: "))
                if amount > 0:
                    balance += amount
                    print(f"${amount} has been deposited. New balance: ${balance}")
                else:
                    print("Invalid amount! Deposit amount must be positive.")

            elif choice == 3:
                amount = float(input("Enter the amount to withdraw: "))
                if amount > 0:
                    if amount <= balance:
                        balance -= amount
                        print(f"${amount} has been withdrawn. Remaining balance: ${balance}")

                else:
                    print("Invalid amount! Withdrawal amount must be positive.")

            elif choice == 4:
                print("Exiting the ATM.")
                break

            else:
                print("Invalid choice! Please choose a valid option.")

        except :
            print("Invalid input")

atm_simulator()
