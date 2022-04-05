# Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
# (If you don’t know what a divisor is, it is a number that divides evenly into another number.
# For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)


def is_divisor(num):
    divisors_of_num = []
    for divisor in range(1, num):
        if num % divisor == 0:
            divisors_of_num.append(divisor)
            print(divisor)
    return divisors_of_num


number = int(input("Please enter a number: "))
print(is_divisor(number))
