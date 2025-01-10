def calculate_loan_payment():
    try:
        principal = float(input("Enter the loan amount (principal): "))
        rate = float(input("Enter the rate of interest (annual): ")) / 100 / 12  
        tenure = int(input("Enter the tenure (in years): ")) * 12  

        if rate == 0:
            monthly_payment = principal / tenure
        else:
            monthly_payment = principal * rate * (1 + rate) ** tenure / ((1 + rate) ** tenure - 1)

        print(f"Your monthly payment is: {monthly_payment:.2f}")

    except ValueError:
        print("Invalid input! Please enter valid numeric values.")
    except ZeroDivisionError:
        print("Interest rate cannot be zero.")

calculate_loan_payment()
