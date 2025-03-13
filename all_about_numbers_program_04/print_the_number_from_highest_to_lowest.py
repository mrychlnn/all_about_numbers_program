# initialize an empty list
numbers = []

# input numbers until the users input is invalid (anything non-numeric)
while True:
    user_input = input("Enter a number (anything non-numeric to stop): ")

    if not user_input.isdigit():
        print("Invalid input.")
        break

# print the numbers from highest to lowest
    num = int(user_input)
    numbers.append(num)

if numbers:
    numbers.sort(reverse=True)
    print("\nNumbers in descending order:", numbers)