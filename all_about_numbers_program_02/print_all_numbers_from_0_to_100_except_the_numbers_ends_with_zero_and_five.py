# print all numbers from 0 to 100
for num in range(101):
    if num % 5 != 0: # skip number ending in 0 and 5
        print(num)