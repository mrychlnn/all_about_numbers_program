# input 2 numbers
num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2nd number: "))

# print all numbers between two numbers inserted by the user
for num in range(num1 + 1, num2):
    print (num, end=" ")