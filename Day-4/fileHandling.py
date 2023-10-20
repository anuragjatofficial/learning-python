# file handling in python

# to open file we need to use open()

# 4 primary modes of opening a file 
    # 1. read mode
    # 2. write mode 
    # 3. delete mode
    # 4. append mode


f = open('Day-4/trial.txt','r')

# print(f.read(10))

# print(f.readline()) # to read a line 

for x in f:
    print(x)

f.close()

# to add text in file 

f = open('Day-4/trial.txt','a')
f.write(" A new line")


f.close()

# open file again to read

f = open('Day-4/trial.txt','r')
print(f.read())

f.close()