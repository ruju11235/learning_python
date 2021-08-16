str = "My name is Rujuta."
print(str)
# print(dir(str))
print()
print("testing 'startswith' function: ")
print('str.startswith("a")', str.startswith("a"))
print()
print("testing 'endswith' function: ")
print('str.endswith(".")', str.endswith("."))
print()
print("testing 'isalpha' function: ")
print('"Kiki".isalpha() = ', "Kiki".isalpha())
print('"Kiki123".isalpha() = ', "Kiki123".isalpha())
print()
print("testing 'isdigit' function: ")
print('"Kiki123".isdigit() = ', "Kiki123".isdigit())
print('"12.3".isdigit() = ', "12.3".isdigit())
print()
print("testing 'isalnum' function: ")
print('"Kiki123".isalnum() = ', "Kiki123".isalnum())
print('str.isalnum() =', str.isalnum())
print()
print("testing 'isnumeric' function: ")
print('"12.3".isnumeric() = ', "12.3".isnumeric())
print()
print("testing 'isspace' function: ")
print('str.isspace() =', str.isspace())
print('"  ".isspace() =', "  ".isspace())

print()
print("testing 'islower' function:")
print('"Kiki".islower() = ', "Kiki".islower())
print('"kiki".islower() = ', "kiki".islower())
print()
print("testing 'isupper' function:")
print('"Kiki".isupper() = ', "Kiki".isupper())
print('"KIKI".isupper() = ', "KIKI".isupper())
print()
print("testing 'istitle' function:")
print('str.istitle() = ', str.istitle())

print()
str = "hello world"
print(str)
print("testing 'capitalize' function:")
print(str.capitalize())
print("testing 'title' function:")
print(str.title())

print("testing 'upper' function:")
print(str.upper())

print()
str = "I love Ice Cream."
print(str)
print("testing 'swapcase' function:")
print(str, str.swapcase())

print("testing 'index' and 'rindex' functions:")
print(str.index("Ice"))
print(str.index("I"))
print(str.rindex("I"))
# The following statements give errors because there is no "!" in the string:
# print(str.index("!"))
# print(str.rindex("!"))


print("testing 'find' and 'rfind' functions:")
print(str.find("I"))
print(str.rfind("I"))
print(str.find("!"))
print(str.rfind("!"))

print()
print("testing 'replace' function:")
print(str.replace(".", "!"))
print(str.replace("Ice", "Whipped"))
print()
print("testing 'count' function:")
print(str.count("I"))
print(str.count("i"))
print(str.count("Ice"))

print()
print("testing 'split' and 'join' funtions:")
words = str.split(" ")
print(words)
print("-".join(words))
print("".join(words))

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