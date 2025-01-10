def classify_number():
    try:
        num = int(input("Enter a number: "))
        
        if num <= 0:
            print(f"{num} is neither prime nor composite.")
        elif num == 1:
            print("1 is neither prime nor composite.")
        else:
            is_prime = True
            for i in range(2, num-1):
                if num % i == 0:
                    is_prime = False
                    break
            
            if is_prime:
                print(f"{num} is a prime number.")
            else:
                print(f"{num} is a composite number.")
    except :
        print("Invalid input! Please enter an integer.")

classify_number()
