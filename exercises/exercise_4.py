# Exercise 4:
# 1. Read a sentence from the user.
# 2. Count how many times letters 'a', 'e', 'i', 'o', 'u' appear in the sentence.
# Please note that these letters could appear in lower case or upper case. You should still count them.
# 3. Print the statement in the title case.
# 4. Find the first and last position where the word 'the' appears in the sentence. It could be written in any case.
# 5. Replace all occurrences of letter 'e' with 'E'.
# 6. When you do the exercise (5) above, does it change the original string?
# Please think about it first, and then use print to check your answer.
# 7. Separate the sentence into words.
# 8. Count how many words there are in the sentence.
# 9. Replace all spaces in the sentence by comma, such that all words should look as if they are joined by comma.
# 10. Take the first word in the sentence. Split it into letters. Print each letter on a line.

sentence = input("Please enter a sentence: ")
vowels = 0

print()
print("Step 2:")
print("- Step 2 using the 'count' function:")
ls = sentence.lower()
print(ls.count("a") + ls.count("e") + ls.count("i") + ls.count("o") + ls.count("u"))
print()
print("- Step 2 using a loop:")
num_vowels = 0
for l in ls:
    if l in "aeiou":
        num_vowels = num_vowels + 1
print(num_vowels)

print()
print("Step 3:")
print(sentence.title())

print()
print("Step 4:")
print(sentence.find("the".lower()))
print(sentence.rfind("the".lower()))
print(sentence.find("the".upper()))
print(sentence.rfind("the".upper()))

print()
print("Step 5:")
print(sentence.replace("e", "E"))

print()
print("Step 7:")
words = sentence.split(" ")
print(words)

print()
print("Step 8:")
num_words = 0
for w in words:
    num_words = num_words + 1
print(num_words)

print()
print("Step 9:")
print(",".join(words))

print()
print("Step 10:")
print(words[0])
for l in words[0]:
    print(l)