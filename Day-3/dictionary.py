# dictionaries in python 
# ----------------------

# keys can't be duplicated
# values are changable 
# we can add or remove item from dictionary


dictionary={
    "name" : "Anurag",
    "age" : 18,
}


print(dictionary["name"]) # or

print(dictionary.get('name'))

dictionary['age'] = 19

dictionary.update({'name':'anurag'})

print(dictionary)


dictionary.pop('name')

print(dictionary)