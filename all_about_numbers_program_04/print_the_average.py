# input numbers until the users input is invalid (anything non-numeric)
while True:
    user_input = input("Enter a number (anything non-numeric to stop): ")

    if not user_input.isdigit():
        print("Invalid input.")
        break

# print the average of entered numbers