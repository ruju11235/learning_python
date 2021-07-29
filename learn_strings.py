str = "Hi! My name is Rujuta."
print(str)

f1 = "ice "
f2 = "cream"
print(f1 + f2)

# age = "ab12cd"
age_str = input("Enter your age. ")
print(age_str)
if age_str.isdigit():
    print("Age is valid.")
else:
    print("Age should be a number.")

word = input("Enter a word. ")
if word.isalpha():
    print("The word is valid")
else:
    print("The word is not valid.")