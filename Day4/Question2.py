# Write a function that takes a number as input and returns its square.

def squareNumber():
    num = int(input("Enter any number: "))
    sqr = num ** 2
    return f"The square of {num} is : {sqr} "
print(squareNumber())