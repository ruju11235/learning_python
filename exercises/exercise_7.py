# Exercise: Ask the user to provide a word and a number. Print the word the same number of times.
# Example:
# Rujuta
# 5
# should print Rujuta 5 times.

word = input("Please enter a word: ")
repeat = int(input("Please enter how many times to repeat your word: "))
count = 0

# exercise with 'while' loop
while count < repeat:
    print(word)
    count += 1

# exercise with 'for' loop


