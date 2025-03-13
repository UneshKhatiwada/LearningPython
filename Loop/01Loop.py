number = [1, 2, -3, -4, 5, 6, -7, 8, -9, 10, -11, 12, -13, -14, 15]
positive_number = 0


for num in number:
    if num>0:
        positive_number +=1
print(f"The total positive number consist in the list is: {positive_number}")