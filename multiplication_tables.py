# Program of Multiplication Tables using a 'for' loop
# - multiples from 0 to 10

num_1 = int(input("Please enter the number to find a multiplication table of: "))
range_start = int(input("Choose the starting range number for the multiples: "))
range_end = int(input("Choose the ending range number for the multiples: "))
print("Multiplication Table of", num_1)
for m in range(range_start, range_end + 1):
    print(num_1, "x", m, "=", num_1 * m)