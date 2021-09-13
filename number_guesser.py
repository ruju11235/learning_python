range_start = int(input("Please enter a starting range number: "))
range_end = int(input("Please enter a ending range number: "))
if range_start or range_end < 0:
    print("Enter a valid values!")
    range_start = int(input("Please enter a starting range number: "))
    range_end = int(input("Please enter a ending range number: "))
num = int(input("Please enter a number for the program to guess: "))

for g in range(range_start, range_end + 1):
    guess = input("Is the guess lower than, greater than, or equal to the guess? ")
    if guess == "lower than":
        print("i am confuseddd")