import math 

def square_function(n):
    return (n**2)

# ans=square_function(4)
# print (ans)

# default value in functions
def area_circle(radius=4):
    return math.pi*radius, 2*math.pi*radius

a,c=area_circle(5)
print("area",a)
print("circum",c)


