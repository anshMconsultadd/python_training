thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

for key,value in thisdict.items():
    print (key,value)


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
y=thisdict.get("model")
print (x,y)

thisdict.update({"color": "red"})

x = thisdict.keys()
del thisdict["year"]
print (thisdict)

 # The clear() method empties the dictionary:
