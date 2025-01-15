
def fibonacci_generator(limit):
    a, b = 0, 1
    for _ in range(limit):
        yield a
        a, b = b, a + b


fib_gen = fibonacci_generator(10)
for num in fib_gen:
    print(num)
