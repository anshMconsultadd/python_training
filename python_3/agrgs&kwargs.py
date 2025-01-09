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



