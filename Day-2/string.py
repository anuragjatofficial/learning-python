# strings in python 

name = 'anurag'

# or

name = "anurag"

# or 

name = """This is a multiline string 
you can take as many line as you want.    """

print(name[1]) # we can acces a character in string with the use of box bracket

print(len(name)) # print lenght of string

print("in" in name) # to check whether a substring is present in a string or not

print(name[2:10]) # to slice string

print(name[:10]) 

# we can use -ve indexing 

print(name[-5:-1])

print(name.upper()) # to upper case

print(name.lower()) # to lower case

print(name.strip()) # remove whitespaces

print(name.replace("in" ,"out")) # replace in with out in string

print(name.split(" ")) # split by space

print(name+name) # concatinate 
