n=int(input("ENTER A NUMER:\t"))
# If given number is greater than 1
if n > 1:
    # Iterate from 2 to n / 2
    for i in range(2, int(n/2)+1):
        # If num is divisible by any number between
        # 2 and n / 2, it is not prime
        if (n % i) == 0:
            print(n, "is not a prime number")
            break
    else:
        print(n, "is a prime number")
else:
    print(n, "is not a prime number")
