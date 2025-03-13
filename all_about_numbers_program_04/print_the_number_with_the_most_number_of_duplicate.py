# initialize a list
numbers = []
# input numbers until the users input is invalid (anything non-numeric)
while True:
    user_input = input("Enter a number (anything non-numeric to stop): ")

    if not user_input.isdigit():
        print("Invalid input.")
        break

# print the number with the most number of duplicate entered by the user
    num = int(user_input)
    numbers.append(num)

if numbers:
    most_frequent = max(set(numbers), key=numbers.count)
    print(f"\nNumber with the most duplicates: {most_frequent}")