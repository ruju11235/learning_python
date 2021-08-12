str = "My Name Is Rujuta."
print(str)
# print(dir(str))
print('str.startswith("a")', str.startswith("a"))
print('str.endswith(".")', str.endswith("."))

print('"Kiki".isalpha() = ', "Kiki".isalpha())
print('"Kiki123".isalpha() = ', "Kiki123".isalpha())
print('"Kiki123".isdigit() = ', "Kiki123".isdigit())
print('"Kiki123".isalnum() = ', "Kiki123".isalnum())
print('str.isalnum() =', str.isalnum())
print('"12.3".isdigit() = ', "12.3".isdigit())
print('"12.3".isnumeric() = ', "12.3".isnumeric())
print('str.isspace() =', str.isspace())
print('"  ".isspace() =', "  ".isspace())

print()

print('"Kiki".islower() = ', "Kiki".islower())
print('"kiki".islower() = ', "kiki".islower())
print('"Kiki".isupper() = ', "Kiki".isupper())
print('"KIKI".isupper() = ', "KIKI".isupper())
print('str.istitle() = ', str.istitle())
print()

str = "hello world"
print(str.capitalize())
print(str.title())
print(str.upper())
print(str)

str = "I love Ice Cream."
print(str, str.swapcase())

# f1 = "ice "
# f2 = "cream"
# print(f1 + f2)
#
# # age = "ab12cd"
# age_str = input("Enter your age. ")
# print(age_str)
# if age_str.isdigit():
#     print("Age is valid.")
# else:
#     print("Age should be a number.")
#
# word = input("Enter a word. ")
# if word.isalpha():
#     print("The word is valid")
# else:
#     print("The word is not valid.")