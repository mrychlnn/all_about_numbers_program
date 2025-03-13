# initialize numbers for list
numbers = []

# input 10 numbers
for i in range(10):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)
    
# print all the unique numbers
print("Unique numbers are:")
for num in numbers:
    if numbers.count(num) == 1:
        print(num, end=" ")