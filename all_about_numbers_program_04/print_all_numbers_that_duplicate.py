# initialize a list
numbers = []

# initialize a set for duplicate number to store
duplicates = set()

# input 10 numbers
for i in range(10):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

# print all duplicate numbers
for num in numbers:
    if numbers.count(num) > 1:
        duplicates.add(num)

if duplicates:
    print("Duplicated numbers are:", duplicates)