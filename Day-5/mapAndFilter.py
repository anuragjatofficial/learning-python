# map and filter function in python
# ---------------------------------

# > map function runs a function on all items in a collection.

collection = [1,2,3,4,5,6]
collection2 = list(map(float,collection)) # using list() to convert it to list again 

print(collection2)

# get double of every value 

collection3 = list(map(lambda x:x*2,collection))

print(collection3)

# > filter function runs a function on all items like map
#  but only stores true values i.e. based on conditions

age = [14,18,12,34,26,89,28,49,38,24,44,]

def adult(x):
    return x>=18

# adults = list(filter(adult,age))

adults = list(filter(lambda x:x>=18,age))


print(adults)