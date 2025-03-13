# initialize an empty list
numbers = []

# input numbers until the users input is invalid (anything non-numeric)
while True:
    user_input = input("Enter a number (anything non-numeric to stop): ")

    if not user_input.isdigit():
        print("Invalid input.")
        break

# print the average of entered numbers
    num = int(user_input)
    numbers.append(num)

if numbers:
    average = sum(numbers) / len(numbers)
    print(f"\nAverage of the entered numbers: {average:.2f}")