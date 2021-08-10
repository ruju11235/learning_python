# Exercise: Ask the user to enter a word.
# Count the number of vowels and number of consonants in the words.
# Do this exercise using some functions.

word = input("Please enter a word: ")
vowels = 0
consonants = 0
numbers = 0
others = 0

for l in word.lower():
    if l.isalpha():
        if l in "aeiou":
            vowels = vowels + 1
        else:
            consonants = consonants + 1
    elif l.isdigit():
        numbers = numbers + 1
    else:
        others = others + 1

print("Number of vowels:", vowels)
print("Number of consonants:", consonants)
print("Number of numbers:", numbers)
print("Other characters:", others)