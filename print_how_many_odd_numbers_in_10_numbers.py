# input 10 numbers
odd_count = 0 

for i in range(10):
    num = int(input(f"Enter number {i + 1}: "))
    if num % 2 != 0:
        odd_count += 1

# print how many odd numbers inserted by the user
print(f"The number of odd numbers are {odd_count}")

