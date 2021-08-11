name = input("What is your name? ")
print("Hello,", name, "!")

print()
age_str = input("How old are you? ")
while not age_str.isdigit():
    print("Why are you being mean to my program? Enter a valid value!!!")
    age_str = input("How old are you? ")

age = int(age_str)
while age < 0:
    print("Why are you being mean to my program? Enter a valid value!!!")
    age = int(input("How old are you? "))
else:
    print("Have fun being", age, "!!!")
    print("Next year you will be", age + 1, ":)")

print()
fav_color = input("What is your favorite color? ")
if fav_color == "green":
    print("My favorite color is also green!")
else:
    print("My favorite color is green!")

print()
fav_food = input("What is your favorite food? ")
if fav_food == "ice cream":
    print("My favorite food is also ice cream!")
else:
    print("My favorite food is ice cream! I can eat however full I am!")
print()
print("Bye!")