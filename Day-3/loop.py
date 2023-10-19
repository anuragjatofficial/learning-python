# loops in python 

    # for loop is used to iterate over lists, sets and truples
    #---------------------------------------------------------

numbers = [1,2,3,4,5,6,7] # list of numbers 

name = "anurag"

# break loop if 5 found in list

for x in numbers:
    print(x)
    if x == 5:
        break

# skip a if present 

for y in name:
    if y == "a":
        continue
    print(y)


# use of range command 

for x in range(40,100):
    print(x)

i = 1
while i < 6:
    print(i)
    i = i+1

