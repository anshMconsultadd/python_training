from assignments.FunctionandModules.q3.math_ops import MathOperations

def main():
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Matrix Multiplication")

    choice = input("Enter choice (1/2/3/4/5): ")

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"The result is: {MathOperations.add(num1, num2)}")
        elif choice == '2':
            print(f"The result is: {MathOperations.subtract(num1, num2)}")
        elif choice == '3':
            print(f"The result is: {MathOperations.multiply(num1, num2)}")
        else :
            try:
                print(f"The result is: {MathOperations.divide(num1, num2)}")
            except ValueError as e:
                print(e)

if __name__ == "__main__":
    main()