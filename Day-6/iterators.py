# iterators in python

# > iterators an object in python which implements iterator protocol

# iterables -> list , tuples , dictinories

tup = ("car", "bike", "aeroplane")

myiter = iter(tup) # iter return an iterator and take list,tuple etc as arguemnts 

# -> we can iterate on a string as well 

print(next(myiter))
print(next(myiter))
print(next(myiter))

for x in tup:
    print(x)

# creating an iterator

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        x = self.a
        self.a += 1
        return x

myClass = MyNumbers()
myIter = iter(myClass)

print(next(myIter))
print(next(myIter))
print(next(myIter)) 
print(next(myIter))
print(next(myIter))
