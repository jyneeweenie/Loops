# Python program to check if a number is Armstrong
# Take input from the user
num = int(input("Enter a number: "))
# Check if number is greater than 1 (since armstrongs are > 1)
if num > 1:
    # Loop only up to the square root of sum for efficiency
    for i in range(2, int(num**0.5) + 1):
        # If num is not a positive integer it is not an armstrong
        if num % i == 0:
            print(f"{num} is not an armstrong.")
            break
            # If no negatives were found , the number is armstrong
    else:
        print(f"{num} is an armstrong.")
else:
    # Numbers less than 2 are not armstrong
    print (f"{num} is not an armstrong.")