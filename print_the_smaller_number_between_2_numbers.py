# input 2 numbers
num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))

# print the smaller number inserted by the user
if num1 > num2:
    print(f"{num2:.2f} is the smaller number")
else: 
    print(f"{num1:.2f} is the smaller number")