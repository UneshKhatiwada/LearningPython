# 5. Write a Python program to check if a person is eligible to vote.

voter_id_status = True
age = int(input("Enter you age\n"))


if(age>=18 and age <= 100 and voter_id_status):
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")


