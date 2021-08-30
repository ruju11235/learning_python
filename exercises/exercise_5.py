# Exercise 5:
# 1. You already know how to multiply two numbers.
# Ask the user to input two numbers and calculate the first number to the power second number.
# e.g. if user types 2 4, calculate 2 * 2 * 2 * 2 = 16.
# 2. Read a sentence and read an alphabet from the user.
# - Print each letter in the sentence on a line.
# - Count the number of occurrences of the alphabet in the sentence and print it.

num_1 = int(input("Please enter a number: "))
num_2 = int(input("Please enter another number: "))
base_number = 1
multiplication_count = 0
while multiplication_count != num_2:
    base_number = base_number * num_1
    multiplication_count = multiplication_count + 1
else:
    print("num_1 to the power num_2 is", base_number)
print(pow(num_1, num_2))

print()
sentence = input("Please enter a sentence: ")
alphabet = input("Please enter a letter: ")
letter_count = 0
for w in sentence.lower():
    print(w)
    if w == alphabet:
        letter_count = letter_count + 1
print()
print("Alphabet occurrences:", letter_count)