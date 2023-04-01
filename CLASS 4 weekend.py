##TUPLE
##a = "a", "b", "a"
##
##for i in a:
##    print(i)
##
##print(a[0], "tuple")
##
##print(type(a))
##print(a)

##SET
##b = {"a", "b", "c", "a"}
##
##
##for i in b:
##    print(i)
##
##print(type(b))
##print(b)


#DICTIONARY METHODS:
##1. clear() - clears the value present inside the dictionary
##car = {
##  "brand": "Ford",
##  "model": "Mustang",
##  "year": 1964
##}
##car.clear()
##print(car)
##Output = {}

##2. copy() - copies the value from another dict
##output = {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

##3. fromkeys() - Assinging same value to all key values
##x = ('key1', 'key2', 'key3')
##y = 0
##a = dict.fromkeys(x, y)
##print(a)
##output = {'key1': 0, 'key2': 0, 'key3': 0}

##4. get() - getting the value from a specific key
##car = {
##  "brand": "Ford",
##  "model": "Mustang",
##  "year": 1964
##}
##x = car.get("model")
##print(x)
##output = Mustang

##5. items() - Return the dictionary's key-value pairs:

##x = car.items()
##print(x)
##output = dict_items([('brand', 'Ford'),
##('model', 'Mustang'), ('year', 1964)])

##6. keys() - return the keys
##x = car.keys()
##print(x)
##output = dict_keys(['brand', 'model', 'year'])

##7. pop() - Remove "model" from the dictionary:
##car.pop("model")
##print(car)
##output = {'brand': 'Ford', 'year': 1964}

##8. popitem() - Remove the last item from the dictionary:
##car.popitem()
##print(car)
##output = {'brand': 'Ford', 'model': 'Mustang'}

##9. setdefault() - Get the value of the "model" item:
##x = car.setdefault("model", "Bronco")
##print(x)
##??

##10. update() - Insert an item to the dictionary:
##car.update({"color": "White"})
##print(car)
##output = {'brand': 'Ford',
##'model': 'Mustang', 'year': 1964, 'color': 'White'}

##11. values() - Return the values:
##x = car.values()
##print(x)
##output = dict_values(['Ford', 'Mustang', 1964])

##Question:
##input apple
##output {"a" : 1, "p" : 2, "l" : 1, "e" : 1}

##input cherry
##output {"c" : 1, "h" : 2, "e" : 1, "r" : 2, "y" : 1}

a="apple"
d={}
for i in a:
    d[i] = d.get(i, 0)
    d[i] = d.get(i) + 1
print(d)

##a="apple"
##d={}
##for i in a:
##    if i not in d:
##        d[i]=0
##        d[i]+=1
##print(d)


##print(a, "input")
##output = {}
##for i in a:
####    output.update({i: a.count(i)})
##    output[i] = a.count(i)
##
##print(output, "ouput")
    

##a="cherry"
##d={}
##for i in a:
##    d[i] = d.setdefault(i,0)+1
##print(d)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
else:
    print("finaly loop completed")


if(True):
    pass
