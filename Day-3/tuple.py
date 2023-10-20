# tuples in python
# ----------------

# to create tuples we need () bracets 
# tuples allow duplicates but we can't change values 

mytuple=('car','bike',3,True)
print(mytuple)

# tuple[3] = 'new bbike' 
#  we will get an error that  'tuple' object does not support item assignment

# we can't change value of tuple directly 
# here is how to do it indirectly 

y=list(mytuple)
y.append('myNewBike')
mytuple=tuple(y)

print(mytuple)