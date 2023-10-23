num = int(input("Enter an integer: "))

string_num = str(num)

reversed_num = ''


for x in range(len(string_num) -1,-1,-1):
    reversed_num += string_num[x]

print(reversed_num) 