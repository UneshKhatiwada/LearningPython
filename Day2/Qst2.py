#2. Write a Python code to check whether a number entered by the user is positive, negative, or zero.

num = int(input("Enter any number:\n"))

if(num<0):
    print(f"{num} is negative")
elif(num>0):
    print(f"{num} is positive")
else:
    print(f"you have entered {num}")
