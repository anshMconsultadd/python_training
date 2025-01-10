def calculate_product(*args):
    product = 1
    for arg in args:
        try:
            num = float(arg)
            product *= num
        except :
            print(f"Non-numeric input detected: {arg}. Skipping this value.")
    return product


result = calculate_product(1, 2, 'a', 3, 4.5)
print(f"The product of the numbers is: {result}")
