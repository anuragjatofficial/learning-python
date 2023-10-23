# Get a list of name as an input from the user and make the first letters in caps and print each word as a list

name_input = input('Enter list of names seperated by space: ')

names = name_input.split()

capitalized_names  = [name.capitalize() for name in names]

for name in capitalized_names:
    print([name])