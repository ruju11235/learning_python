# start = int(input("Give a valid starting value! "))
# end = int(input("Give a valid ending value! "))
# while start > end:
#     print("Stop being mean to my program >:(")
#     start = int(input("Give a valid starting value! "))
#     end = int(input("Give a valid ending value! "))
#
# n = start
# while n < end:
#     print(n)
#     n = n + 1
# print()
#
# infinite loop
# n = start
# while n <= end:
#     print(n)
#     n = n - 1
#
# n = start
# step = int(input("How much would you like to increment by? "))
# while n < end:
#     print(n)
#     n = n + step
# print()
#
# for i in range(start, end):
#     print(i)
# print()
#
# for i in range(start, end, step):
#     print(i)
# print()

name = input("Please enter your name: ")
for x in name:
    if x in ("A", "E", "I", "O", "U", "a", "e", "i", "o", "u"):
        print(x, "vowel")
    elif x .isdigit():
        print()
    else:
        print(x, "consonant")
