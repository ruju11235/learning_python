dividend = int(input("Please enter a number: "))
divisor = int(input("Please enter another number: "))
quotient = dividend // divisor
remainder = dividend % divisor

print()
if dividend < divisor:
    print(dividend, "is the remainder.")
else:
    print("The answer to your question is", quotient)
    print("The remainder is", remainder)