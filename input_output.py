name = input("What is your name? ")
print("Hello,", name, "!")

print()
age = int(input("How old are you? "))
while age < 0:
    print("Why are you being mean to my program? Enter a valid value!!!")
    age = int(input("How old are you? "))
else:
    print("Have fun being", age, "!!!")
    print("Next year you will be", age + 1, ":)")

print()
favc = input("What is your favorite color? ")
if favc == "green":
    print("My favorite color is also green!")
else:
    print("My favorite color is green!")

print()
favf = input("What is your favorite food? ")
if favf == "ice cream":
    print("My favorite food is also ice cream!")
else:
    print("My favorite food is ice cream! I can eat however full I am!")
print("")
print("Bye!")
