def is_prime(n):
    status = True
    if n < 2:
        status = False
    else:
        for i in range(2,n):
            if n % i == 0:
                status = False
    return status
smallNumber = int(input("Enter a number: "))  
largeNumber = int(input("Enter a number: "))  
for n in range(smallNumber,largeNumber):
    if is_prime(n):
        if n==97:
            print(n)
        else:
            print(n,",")