start = int(input("Give a valid starting value! "))
end = int(input("Give a valid ending value! "))
while start > end:
    print("Stop being mean to my program >:(")
    start = int(input("Give a valid starting value! "))
    end = int(input("Give a valid ending value! "))

n = start
while n <= end:
    print(n)
    n = n + 1
print()

# infinite loop
# n = start
# while n <= end:
#     print(n)
#     n = n - 1

n = start
step = int(input("How much would you like to increment by? "))
while n <= end:
    print(n)
    n = n + step