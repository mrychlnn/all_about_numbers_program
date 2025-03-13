# initialize set for unique numbers
numbers = set()  

# input numbers until the users input is invalid (anything non-numeric)
while True:
    user_input = input("Enter a number (anything non-numeric to stop): ")

    if not user_input.isdigit():
        print("Invalid input.")
        break

# print "Unique" for numbers that don't have duplicate and "Duplicate" for numbers that have duplicate (side of the numbers) 
    num = int(user_input)

    if num in numbers:
        print("Duplicate")
    else:
        print("Unique")
        numbers.add(num)  