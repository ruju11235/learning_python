age = int(input("How old are you? "))
if age < 13:
    print("child")
elif age <= 19:
    print("teenager")
elif age <= 64:
    print("adult")
elif age <= 130:
    print("senior citizen")
else:
    print("dead")