# Develop a program to take user input for multiple numbers, store
# them in a list, and compute basic statistical metrics like mean,
# median, mode, and standard deviation.
import statistics
def calcstatistics():
    try:
        numbers = input("Enter numbers separated by space: ").split()
        numbers = [float(num) for num in numbers]

        mean = statistics.mean(numbers)
        median = statistics.median(numbers)
        mode = statistics.mode(numbers)
        stdev = statistics.stdev(numbers)

        print(f"Mean: {mean}")
        print(f"Median: {median}")
        print(f"Mode: {mode}")
        print(f"Standard Deviation: {stdev}")

    except :
        print("Invalid input! Please enter numeric values.")


calcstatistics()
