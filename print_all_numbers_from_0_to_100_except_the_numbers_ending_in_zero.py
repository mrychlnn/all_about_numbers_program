# print all the numbers from 0 to 100 
for num in range(101):
    if num % 10 != 0: # skip numbers that ends with zero
        print(num)