# Write a Python code to read an integer in a file 
# e.g 123 and convert it to words e.g One hundred 
# and twenty three and write the result back to the 
# same file such that your file will have "123 One 
# hundred and twenty three " in it

with open("numFile.txt", "r") as file:
    number = int(file.read())

number_in_words = "One hundred and twenty three"

with open("numFile.txt", "a") as file:
    file.write(" " + number_in_words)

print(number_in_words)
