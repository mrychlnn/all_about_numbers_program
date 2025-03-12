# input 10 numbers
total = 0

for i in range(10):
    num = float(input(f"Enter number {i + 1}: "))
    total += num

# print the sum of all the numbers
print(f"The sum of all numbers is {total:.2f}")
