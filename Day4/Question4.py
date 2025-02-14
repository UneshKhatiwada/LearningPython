# Write a function that returns the largest of three numbers.

def largest_number(a,b,c):
    if(a>b and a>c):
        print("A is the largest number among all.")
    elif(b>c and b>c):
        print("B is the largest number among all.")
    else:
        print("C is the largest number among all.")
largest_number(a=2,b=10,c=3)