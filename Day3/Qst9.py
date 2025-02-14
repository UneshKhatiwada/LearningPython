# 9. Write a program that takes a list of numbers and prints True if all numbers are positive, otherwise False.

number = [-1,2,3,4,5,-6,7,8,9,-2,-3,10,-5]

for num in number:
    if(num>0):
        print(f"True, {num} is positive")
    else:
        print(f"False, {num} is negative")