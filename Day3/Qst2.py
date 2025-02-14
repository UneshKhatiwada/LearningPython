# 2. Write a program that takes a list of numbers and finds the sum of all even numbers in the list.

num = list(range(1,100))

sum_of_even = 0

for i in range(len(num)): 
    if num[i] % 2 == 0:
        sum_of_even+=num[i]
print(f"The sum of all given even number is {sum_of_even}")
      

    
