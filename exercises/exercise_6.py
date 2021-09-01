# Exercise 6:
# 1. You already know how to multiply two numbers.
# Ask the user to input two numbers and calculate the first number to the power second number.
# e.g. if user types 2 4, calculate 2 * 2 * 2 * 2 = 16.
# - Write it with a 'for' loop.

num_1 = int(input("Please enter a number: "))
num_2 = int(input("Please enter another number: "))
if num_1 == 0 and num_2 < 0:
    print("This value is undefined!")
    exit(0)

if num_2 >= 0:
    start, end, step = 1, num_2 + 1, 1
else:
    start, end, step = -1, num_2 - 1, -1
base_number = 1
operation_count = 0

for operation_count in range(start, end, step):
    if num_2 >= 0:
        base_number = base_number * num_1
    else:
        base_number = base_number / num_1
else:
    print("num_1 to the power num_2 is", base_number)
print(pow(num_1, num_2))