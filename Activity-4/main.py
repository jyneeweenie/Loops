# Python program to check if a number is prime
# Take input from the user
num = int(input("Enter a number: "))
# Check if number is greater than 1 (since primes are > 1)
if num > 1:
    # Loop only up to the square root of sum for efficiency
    for i in range(2, int(num**0.5) + 1):
        # If num is divisible by any number , it's not prime
        if num % i == 0:
            print(f"{num} is not a prime number.")
            break
            # If no divisors were found , the number is prime
    else:
        print(f"{num} is a prime number.")
else:
    # Numbers less than 2 are not prime
    print (f"{num} is not a prime number.")