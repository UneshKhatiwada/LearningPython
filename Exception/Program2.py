num = [1,2,3,4,5]

try:
    print(num[5])
except IndexError as e:
    print("Invalid index of list")
