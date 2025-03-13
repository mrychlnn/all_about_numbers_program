# input 1st number
result = float(input("Enter number 1: "))

# input the remaining numbers (9 numbers)
for i in range(2, 11):
    num = float(input(f"Enter number {i}: "))
    result -= num

# print the result when 1st number minus all of the remaining numbers inserted by the user
print(f"The result after subtracting the remaining numbers is {result:.2f}")