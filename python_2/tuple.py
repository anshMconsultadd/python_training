thistuple= ("ansh","divyansh","ayush")
# To create a tuple with a single element, you need to include a trailing comma:
newtuple=("arpit",)
thistuple=thistuple+newtuple
print(thistuple)


# Convert the tuple into a list to be able to change it:

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

#  list to tiple for appending in tuple

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

 # When we create a tuple, we normally assign values to it. This is called "packing" a tuple:
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)