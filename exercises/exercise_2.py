# Exercise: Select a word, store it in some variable. Ask the user to enter a word.
# While the word is not the same as the word you selected, keep asking the user to enter a word.
# Stop when the two words are the same.

my_word = "gymnastics"
user_word = input("Enter a word: ")
while my_word != user_word:
    user_word = input("Enter a word: ")
else:
    print("Thank you!")