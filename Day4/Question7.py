# Write a function that takes a list of numbers and returns the sum of all the numbers.

def sumOfList():
    sum_of_list = 0
    num = list(range(1,10))
    for n in range(len(num)):
        sum_of_list+=num[n]
    print(f"The sum of list is {sum_of_list}")
sumOfList()
        