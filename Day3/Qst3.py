# 3. Write a program that takes a list of numbers and counts how many numbers are greater than 50

num = list(range(1,100))

count_num = 0

for n in num:
    if(n>50):
        count_num+=1
print(f"The total number is greater than 50 is : {count_num}")



        