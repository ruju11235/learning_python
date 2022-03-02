# Exercise: Ask the user to provide a letter and a number. Print the letter in the following format.
# Example:
# a
# 4
# Output:
# a
# aa
# aaa
# aaaa

letter = input("Please enter a letter: ")
num = int(input("Please enter a number: "))
count = 1

while count < num + 1:
    print(letter*count)
    count += 1