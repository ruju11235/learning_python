# Exercise: Read two numbers from the user. Divide the first number by the second number.
# Print the quotient and the remainder. Do not use direct division. Do this by repeated subtraction.
# Examples.
# 11
# 3
# You repeatedly subtract 3 from 11. Count how many times you have subtracted until you can find quotient and remainder.
# Try a few examples on paper before you write the program.

num_1 = int(input("Please enter a integer: "))
num_2 = int(input("Please enter another integer: "))
q = 0

while num_1 >= num_2:
    num_1 = num_1 - num_2
    q = q + 1
print("Quotient:", q)
print("Remainder:", num_1)
