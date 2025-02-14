# 4. Write a Python program to find the largest of three numbers.


firstNum = int(input("Enter the first number:\n"))
secondNum = int(input("Enter the second number:\n"))
thirdNum = int(input("Enter the third number:\n"))


if(firstNum > secondNum and firstNum > thirdNum):
    print(f"{firstNum} is the largest among all")
elif(secondNum > firstNum and secondNum > thirdNum):
    print(f"{secondNum} is the largest among all")
else:
    print(f"{thirdNum} is the largest all")