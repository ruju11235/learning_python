# Exercise: Ask the user to enter a word.
# Count the number of vowels and number of consonants in the words.

word = input("Please enter a word: ")
v = 0
c = 0
for l in word:
    if l in ("A", "E", "I", "O", "U", "a", "e", "i", "o", "u"):
        v = v + 1
    else:
        c = c + 1

print("Number of vowels:", v)
print("Number of consonants:", c)