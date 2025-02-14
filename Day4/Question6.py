# Write a function that calculates the factorial of a given number.

def factorial_calculater(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

num = int(input("Enter a any number: "))
print(f"The factorial of {num} is {factorial_calculater(num)}")

