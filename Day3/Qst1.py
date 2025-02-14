# 1. Write a program that takes a list of numbers and prints "Odd" if the number is odd and "Even" if the number is even.

num = list(range(1,100))

for i in range(len(num)): 
    if num[i] % 2 != 0:
        print(f"{num[i]} is odd")
    else:
        print(f"{num[i]} is even ")

    
