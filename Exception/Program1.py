is_valid = False

while(is_valid == False):
    integer = input("Enter a valid number: ")
    try:
        integer_2 = int(integer)
        print("This is correct integer : ", integer_2)
        is_valid = True
        #break
    except ValueError as e:
        is_valid = False
        print("Try Again")