# Program of Multiplication Tables using a 'for' loop
# - multiples from 0 to 10

# num_1 = int(input("Please enter the number to find a multiplication table of: "))
# range_start = int(input("Choose the starting range number for the multiples: "))
# range_end = int(input("Choose the ending range number for the multiples: "))
# print("Multiplication Table of", num_1)
# for m in range(range_start, range_end + 1):
#     print(num_1, "x", m, "=", num_1 * m)

start_num = int(input("Please enter a number to find a multiplication table of: "))
end_num = int(input("Please enter another number: "))
start_multiple = int(input("Please which number to start the multiples from: "))
end_multiple = int(input("Please which number to end the multiples: "))

for m in range(start_num, end_num + 1):
    print()
    print("Multiplication Table of", m)
    for n in range(start_multiple, end_multiple + 1):
        print(m, "x", n, "=", m * n)