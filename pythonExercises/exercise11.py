# Ask the user for a number and determine whether the number is prime or not.
# (For those who have forgotten, a prime number is a number that has no divisors.).
# You can (and should!) use your answer in Exercise 4 to help you.
# Take this opportunity to practice using functions, described below


def is_divisor(num, divisor):
    return num % divisor == 0


def is_prime(num):
    count = 0
    for i in range(2, num):
        if is_divisor(num, i):
            count += 1
    if count == 0:
        return True
    else:
        return False


prime_number = int(input("Please enter a number: "))
print(is_prime(prime_number))

