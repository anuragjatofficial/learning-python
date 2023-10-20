# classes are blue print for object 
# instead of constructor like java or other languages 
# we have init mehod to make objects in python

class Human:

    # self param is the reference to 
    # current instance of the class

    def __init__(self,name,age):
        self.name  = name
        self.age = age

    def methods(self):
        print('hi my name is ' + self.name)


h1 = Human("Anurag", 19)

print(h1.name)

h1.methods()


# we can modify the values of object 

h1.name = "jatin"

h1.methods()

del h1 # to delete any object in python 


# in python we can't have empty class so 
# we can take use of pass keyword instead

class Name:
    pass
