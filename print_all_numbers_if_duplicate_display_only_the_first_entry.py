# initialize an empty list
numbers = []

# initialize set keep track for the seen numbers
seen = set()

# input 10 numbers
for i in range(10):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

# print all numbers if duplicate display only the 1st entry