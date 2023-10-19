a = 33
b = 200

if a>b:
    print("a is greater")
elif a == b:
    print("both are equal")
else:
    print("b is greater")
    
# or we can write it another way


print("a is greater ") if a>b else print("b is greater")

c = 500

if a<b and c>b: # and statement
    print("a is less than b and b is less than c ")
else:
    print("else part") 

if a>b or c>b:
    print("inside if block")
else:
    print("inside else block")