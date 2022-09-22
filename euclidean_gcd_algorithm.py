

a = int(input("Please enter a number which is greater than or equal to 0: "))
b = int(input("Please enter another number greater than 0: "))
q = int(a/b)
r = (a % b)

while r != 0:
    a = b
    b = r
    q = int(a/b)
    r = a - (b * q)
print(b)