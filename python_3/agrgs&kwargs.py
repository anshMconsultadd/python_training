# In Python, *args and **kwargs are used to allow 
# functions to accept an arbitrary number of arguments. 
# These features provide great flexibility when designing functions 
# that need to handle a varying number of inputs.

def sum_all(*args):
    print(type(args))
    sum=0
    for i in args:
        sum=sum+i
    return sum

print(sum_all(1,2,3,4))
print(sum_all(1,2,3,4,5,6,7,8))

def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_info(name="Ansh", age=25, city="Mumbai")


def greet(*args):
    for name in args:
        print(f"Hello, {name}!")

greet("Ansh", "Divyansh", "Ayush")  
# Output:
# Hello, Ansh!
# Hello, Divyansh!
# Hello, Ayush!

# keywords argyumensts kwargs

def intro(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")

intro(name="ansh",age=21,intrests="storytelling")



def fun(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

fun(1, 2, 3, a=4, b=5)

def intro_more(*args,**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")

