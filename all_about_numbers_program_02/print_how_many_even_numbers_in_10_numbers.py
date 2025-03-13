# initialize the count of even numbers
even_count = 0 

# input 10 numbers
for i in range(10):
    num = int(input(f"Enter number {i + 1}: "))
    if num % 2 == 0:
        even_count += 1

# print how many even numbers in 10 numbers inserted by the user
print(f"The number of even numbers are {even_count}")