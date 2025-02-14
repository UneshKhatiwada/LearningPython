# DRY Principle
def user_input():
    return int(input("Enter a number : "))

def calculate(a,b):
    sum = a + b
    difference = a - b
    products = a * b
    division = a/b
    return sum, difference, products, division

a = user_input()
b = user_input()
print("a is", a, ", b is",b)

sum , difference, products, division = calculate(a,b)


print("Sum of the two number is :" , sum)
print("Subtraction between two digits is : ",difference)
print("Multiplication of two numbers is: ",products)
print("Division of two number is: ",division)