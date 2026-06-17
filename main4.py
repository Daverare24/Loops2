# Take an integer input from the user
number = int(input("Enter a number: "))

# Check if the number is greater than 1
if number > 1:

    # Test divisors from 2 to √number
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            print("not a prime number")
            break
    else:
        print("is a prime number")

# Numbers less than or equal to 1 are not prime
else:
    print("not a prime number")