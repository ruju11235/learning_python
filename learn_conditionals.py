name = input("What is your name? ")

age = int(input("How old are you? "))
if age < 0:
    print(name, "is in the future!")
elif age < 13:
    print(name, "is a child!")
elif age <= 19:
    print(name, "is a teenager!")
elif age <= 64:
    print(name, "is an adult!")
elif age <= 130:
    print(name, "is a senior citizen!")
else:
    print(name, "is dead :)")