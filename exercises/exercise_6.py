# Exercise 6:
# 1. You already know how to multiply two numbers.
# Ask the user to input two numbers and calculate the first number to the power second number.
# e.g. if user types 2 4, calculate 2 * 2 * 2 * 2 = 16.
# - Write it with a 'for' loop.

num_1 = int(input("Please enter a number: "))
num_2 = int(input("Please enter another number: "))
base_number = 1
operation_count = 0

# for:
#     if num_2 < 0:
#         base_number = base_number / num_1
#         operation_count = operation_count - 1
#     else:
#         base_number = base_number * num_1
#         operation_count = operation_count + 1