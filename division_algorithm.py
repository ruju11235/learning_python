dividend = int(input("Please enter a number: "))
divisor = int(input("Please enter another number: "))
if dividend == 0 or divisor == 0:
    print("Please give a valid value next time!")
    exit(0)
quotient = dividend // divisor
remainder = dividend % divisor

print()
# The Division Algorithm using conditionals
if dividend < divisor:
    print("The quotient is 0.")
    print(dividend, "is the remainder.")
else:
    print("The quotient is", quotient)
    print("The remainder is", remainder)

print()
num_1 = dividend
num_2 = divisor
q = 0
# The Division Algorithm using a 'while' loop
while num_1 >= num_2:
    num_1 = num_1 - num_2
    q = q + 1
else:
    print("The quotient is", q)
    print(num_1, "is the remainder.")