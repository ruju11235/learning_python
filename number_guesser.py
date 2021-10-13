range_start = int(input("Please enter a starting range number: "))
range_end = int(input("Please enter a ending range number: "))
if range_start or range_end < 0:
    print("Enter a valid values!")
    range_start = int(input("Please enter a starting range number: "))
    range_end = int(input("Please enter a ending range number: "))