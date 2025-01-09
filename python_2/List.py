# varities in lists 
consultadd= ['Finance','Marketing','Engineering']
print(consultadd[1:3])
print(consultadd[1:1])
consultadd[1:1]=["legal"]
print(consultadd)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

consultadd.pop()
for dept in consultadd:
    print(dept)

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

# list comprehnesion 
print([x**2 for x in range(10)])

import copy
consultadd_unoffcial=copy.deepcopy(consultadd)
consultadd[1:2]=["CEO"]
print(consultadd)
print(consultadd_unoffcial)

newlist = [x for x in range(10) if x < 5]
print(newlist)


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
