name = input("What is your name? ")
print("Hello,", name)

age = int(input("How old are you? "))
while age < 0:
    print("Why are you being mean to my program? Enter a valid value!!!")
    age = int(input("How old are you? "))
else:
    print("Have fun being", age)
    print("Next year you will be", age+1)

favc = input("What is your favorite color? ")
print("My favorite color is green!")

favf = input("What is your favorite food? ")
print("My favorite food is ice cream! I can eat however full I am!")

print("Bye!")