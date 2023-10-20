# list comprehension

fruits = ['apples','bananas','pineapples','mango']

myFruits = [x for x in fruits if 'an' in x ]

print(myFruits)

newFruits = [x.upper() for x in fruits ]

print(newFruits)


someExtraFruits = [x if x !='apples' else 'oranges' for x in fruits]

print(someExtraFruits)