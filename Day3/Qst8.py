# 8. Write a program that takes a list of numbers and prints the numbers that are divisible by 3.

number = list(range(1,50))


for num in number:
    if(num % 3 == 0):
        print(num)

    