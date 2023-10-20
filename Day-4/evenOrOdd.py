n = 2
def primeOrNot(n):
    count = 0
    for i in range(1,n+1):
        print(i)
        if n % i == 0:
            count = count +1

    if count==2:
        print("number is prime")
    
    else:
        print("number is not prime")

primeOrNot(n)